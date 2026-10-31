import os
import glob
import struct
import subprocess
from PIL import Image

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
assets_dir = os.path.join(base_dir, "assets")
usm_pattern = os.path.join(assets_dir, "Data", "Video", "**", "*.usm")
usm_files = glob.glob(usm_pattern, recursive=True)

print(f"Found {len(usm_files)} USM files to process.")

def demux_usm_to_ivf(usm_path):
    with open(usm_path, "rb") as f:
        data = f.read()

    file_size = len(data)
    offset = data.find(b"CRID")
    if offset < 0:
        return None

    chunks = []
    known = [b"CRID", b"@SFV", b"@SFA", b"@ALP", b"@SBT", b"@CUE", b"@UTF"]

    while offset + 8 <= file_size:
        magic = data[offset : offset + 4]
        if magic not in known:
            break
        block_size = struct.unpack(">I", data[offset + 4 : offset + 8])[0]

        if magic == b"@SFV" and offset + 0xE <= file_size:
            h_sz = struct.unpack(">H", data[offset + 8 : offset + 10])[0]
            f_sz = struct.unpack(">H", data[offset + 10 : offset + 12])[0]
            if block_size > h_sz + f_sz:
                p_start = offset + 8 + h_sz
                p_end = offset + 8 + block_size - f_sz
                if p_end <= file_size:
                    chunks.append(data[p_start:p_end])

        offset += 8 + block_size

    # Extract VP9 payload from DKIF to #CONTENTS END
    payload = bytearray()
    started = False
    for c in chunks:
        if not started:
            if c.startswith(b"DKIF"):
                started = True
                payload.extend(c)
        else:
            if c.startswith(b"#CONTENTS END"):
                break
            payload.extend(c)

    return bytes(payload) if started else None

results = []

for usm_path in sorted(usm_files):
    fname = os.path.basename(usm_path)
    base_name = os.path.splitext(fname)[0]
    file_dir = os.path.dirname(usm_path)

    print(f"Processing: {fname}...")
    ivf_data = demux_usm_to_ivf(usm_path)
    if not ivf_data:
        print(f"  [!] Failed to extract IVF from {fname}")
        continue

    temp_ivf = os.path.join(file_dir, f"{base_name}.tmp.ivf")
    mp4_path = os.path.join(file_dir, f"{base_name}.mp4")
    thumb_path = os.path.join(file_dir, f"{base_name}_thumb.png")

    with open(temp_ivf, "wb") as f:
        f.write(ivf_data)

    # 1. Convert IVF to MP4 (H.264, faststart, yuv420p)
    cmd_mp4 = [
        "ffmpeg", "-y", "-i", temp_ivf,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        mp4_path
    ]
    p_mp4 = subprocess.run(cmd_mp4, capture_output=True, text=True)
    if p_mp4.returncode != 0:
        print(f"  [!] FFmpeg MP4 error: {p_mp4.stderr[:200]}")
    else:
        print(f"  [+] Generated MP4: {os.path.basename(mp4_path)} ({os.path.getsize(mp4_path)} bytes)")

    # 2. Extract representative thumbnail (frame at 0.5s or frame 1)
    cmd_thumb = [
        "ffmpeg", "-y", "-ss", "00:00:00.500", "-i", temp_ivf,
        "-vframes", "1",
        thumb_path
    ]
    p_thumb = subprocess.run(cmd_thumb, capture_output=True, text=True)
    if p_thumb.returncode != 0 or not os.path.exists(thumb_path) or os.path.getsize(thumb_path) == 0:
        # Fallback to first frame
        cmd_thumb_fallback = [
            "ffmpeg", "-y", "-i", temp_ivf,
            "-vframes", "1",
            thumb_path
        ]
        subprocess.run(cmd_thumb_fallback, capture_output=True, text=True)

    if os.path.exists(thumb_path) and os.path.getsize(thumb_path) > 0:
        im = Image.open(thumb_path)
        w, h = im.size
        print(f"  [+] Generated Thumbnail: {os.path.basename(thumb_path)} ({w}x{h}, {os.path.getsize(thumb_path)} bytes)")
        results.append({
            "usm": usm_path,
            "mp4": mp4_path,
            "thumb": thumb_path,
            "width": w,
            "height": h
        })
    else:
        print(f"  [!] Failed to generate thumbnail for {fname}")

    # Remove temporary IVF
    if os.path.exists(temp_ivf):
        os.remove(temp_ivf)

print(f"\nCompleted processing {len(results)}/{len(usm_files)} USM videos.")

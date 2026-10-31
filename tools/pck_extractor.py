import os
import struct
import glob

def extract_pck(pck_path, out_dir, target_ids=None):
    """
    Extracts .wem or .bnk files from a Wwise .pck file.
    If target_ids is provided, only extracts files whose ID is in target_ids.
    """
    os.makedirs(out_dir, exist_ok=True)
    extracted = []

    with open(pck_path, 'rb') as f:
        magic = f.read(4)
        if magic != b'AKPK':
            return extracted
        
        header_size, unk1, lang_size, bnk_size, stream_size, ext_size = struct.unpack('<IIIIII', f.read(24))
        
        # Read lang table
        f.seek(28)
        lang_data = f.read(lang_size)

        # 1. Banks table
        if bnk_size > 0:
            f.seek(28 + lang_size)
            bnk_count = struct.unpack('<I', f.read(4))[0]
            for _ in range(bnk_count):
                fid, bsize, fsize, foff, lid = struct.unpack('<IIIII', f.read(20))
                if target_ids is None or fid in target_ids:
                    pos = f.tell()
                    f.seek(foff)
                    data = f.read(fsize)
                    f.seek(pos)
                    out_path = os.path.join(out_dir, f"{fid}.bnk")
                    with open(out_path, 'wb') as out_f:
                        out_f.write(data)
                    extracted.append((fid, out_path, fsize))

        # 2. Streams table
        if stream_size > 0:
            f.seek(28 + lang_size + bnk_size)
            stream_count = struct.unpack('<I', f.read(4))[0]
            for _ in range(stream_count):
                fid, bsize, fsize, foff, lid = struct.unpack('<IIIII', f.read(20))
                if target_ids is None or fid in target_ids:
                    pos = f.tell()
                    f.seek(foff)
                    data = f.read(fsize)
                    f.seek(pos)
                    out_path = os.path.join(out_dir, f"{fid}.wem")
                    with open(out_path, 'wb') as out_f:
                        out_f.write(data)
                    extracted.append((fid, out_path, fsize))

        # 3. External sources table
        if ext_size > 0:
            f.seek(28 + lang_size + bnk_size + stream_size)
            ext_count = struct.unpack('<I', f.read(4))[0]
            for _ in range(ext_count):
                fid, bsize, fsize, foff, lid = struct.unpack('<QIIII', f.read(24))
                if target_ids is None or fid in target_ids:
                    pos = f.tell()
                    f.seek(foff)
                    data = f.read(fsize)
                    f.seek(pos)
                    out_path = os.path.join(out_dir, f"{fid}.wem")
                    with open(out_path, 'wb') as out_f:
                        out_f.write(data)
                    extracted.append((fid, out_path, fsize))

    return extracted

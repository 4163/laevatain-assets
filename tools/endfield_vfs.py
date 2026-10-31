import struct
import binascii
import os
import sys
from typing import List, Dict, Optional, Tuple
from Crypto.Cipher import ChaCha20

KEY = bytes([
    0xE9, 0x5B, 0x31, 0x7A, 0xC4, 0xF8, 0x28, 0x56,
    0x9D, 0x23, 0xA8, 0x6B, 0xF2, 0x71, 0xDC, 0xB5,
    0x3E, 0x84, 0x6F, 0xA7, 0x5C, 0x92, 0x4D, 0x67,
    0x1D, 0xBA, 0x8E, 0x38, 0xF4, 0xCA, 0x52, 0xE1
])

PROTOCOL_VERSION = 3

def parse_blc(blc_path: str) -> Tuple[str, List[Dict]]:
    with open(blc_path, 'rb') as f:
        file_bytes = f.read()
    if len(file_bytes) < 12:
        return "", []

    nonce = file_bytes[:12]
    cipher = ChaCha20.new(key=KEY, nonce=nonce)
    cipher.seek(64)
    plain = cipher.decrypt(file_bytes[12:])

    pos = 0
    def read(n: int) -> bytes:
        nonlocal pos
        res = plain[pos:pos+n]
        pos += n
        return res

    code_version = struct.unpack('<i', read(4))[0]
    if code_version > 10:
        code_version = 3
    else:
        version = struct.unpack('<i', read(4))[0]

    name_len = struct.unpack('<H', read(2))[0]
    group_name = read(name_len).decode('utf-8', errors='replace')
    group_hash = binascii.hexlify(read(4)).decode('utf-8').upper()
    read(4)  # padding
    info_num = struct.unpack('<i', read(4))[0]
    chunks_len = struct.unpack('<q', read(8))[0]
    block_type = read(1)[0]
    chunk_count = struct.unpack('<i', read(4))[0]

    def read_tag(cver: int):
        if cver >= 5:
            read(8)
        elif cver > 3:
            read(4)

    files = []
    base_dir = os.path.dirname(blc_path)
    for _ in range(chunk_count):
        chk_md5 = binascii.hexlify(read(16)).decode('utf-8').upper()
        content_md5 = binascii.hexlify(read(16)).decode('utf-8').upper()
        c_len = struct.unpack('<q', read(8))[0]
        c_type = read(1)[0]
        read_tag(code_version)
        file_count = struct.unpack('<i', read(4))[0]
        for _ in range(file_count):
            fn_len = struct.unpack('<H', read(2))[0]
            fn = read(fn_len).decode('utf-8', errors='replace')
            name_hash = read(8)
            chk_md5_2 = read(16)
            data_md5 = read(16)
            offset = struct.unpack('<q', read(8))[0]
            length = struct.unpack('<q', read(8))[0]
            f_type = read(1)[0]
            b_enc = read(1)[0] != 0
            iv_seed = struct.unpack('<q', read(8))[0] if b_enc else 0
            read_tag(code_version)
            files.append({
                'name': fn,
                'chk': chk_md5,
                'offset': offset,
                'length': length,
                'enc': b_enc,
                'iv': iv_seed,
                'vfs_dir': base_dir,
                'group': group_name
            })
    return group_name, files

def extract_vfs_file(file_entry: Dict) -> bytes:
    chk_name = f"{file_entry['chk']}.chk"
    chk_path = os.path.join(file_entry['vfs_dir'], chk_name)
    if not os.path.exists(chk_path):
        # Try fallback to StreamingAssets if vfs_dir is in Persistent
        alt_dir = file_entry['vfs_dir'].replace(os.path.join('Endfield_Data', 'Persistent'), os.path.join('Endfield_Data', 'StreamingAssets'))
        alt_path = os.path.join(alt_dir, chk_name)
        if os.path.exists(alt_path):
            chk_path = alt_path
        else:
            # Try reverse: if vfs_dir was StreamingAssets, check Persistent
            alt_dir2 = file_entry['vfs_dir'].replace(os.path.join('Endfield_Data', 'StreamingAssets'), os.path.join('Endfield_Data', 'Persistent'))
            alt_path2 = os.path.join(alt_dir2, chk_name)
            if os.path.exists(alt_path2):
                chk_path = alt_path2
            else:
                raise FileNotFoundError(f"Chunk file not found: {chk_name} in {file_entry['vfs_dir']} or {alt_dir}")

    with open(chk_path, 'rb') as f:
        f.seek(file_entry['offset'])
        data = f.read(file_entry['length'])
    if file_entry['enc']:
        nonce = struct.pack('<I', PROTOCOL_VERSION) + struct.pack('<q', file_entry['iv'])
        cipher = ChaCha20.new(key=KEY, nonce=nonce)
        cipher.seek(64)
        data = cipher.decrypt(data)
    return data

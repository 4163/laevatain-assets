# Proprietary and custom extraction tooling

This directory contains custom utilities and scripts created for extracting, decrypting, and parsing assets from **Arknights: Endfield** (v1.6.3).

## Tool inventory

| File | Language | Purpose | Upstream / Reference |
|---|---|---|---|
| [`endfield_vfs.py`](endfield_vfs.py) | Python | Virtual File System (`.blc` / `.chk`) parser and ChaCha20 chunk block decryptor | Custom VFS protocol implementation |
| [`endfield_bundle_crypto.py`](endfield_bundle_crypto.py) | Python | Unity AssetBundle header XOR and SBox decryption | Endfield bundle encryption protocol |
| [`deserialize_assets.py`](deserialize_assets.py) | Python | UnityPy automated extraction of meshes (OBJ/FBX), textures (PNG), and animations | [UnityPy](https://github.com/K0lb3/UnityPy) |
| [`process_usm.py`](process_usm.py) | Python | CRI Sofdec USM video stream demuxing into VP9 IVF and H.264 MP4 conversion | CRI Sofdec Demuxer specification |
| [`BatchBundleUnpacker.cs`](BatchBundleUnpacker.cs) | C# | Multi-threaded batch bundle unpacker wrapper built against AnimeStudio engine | [AnimeStudio](https://github.com/Escartem/AnimeStudio) |
| [`SparkBuffer.cs`](SparkBuffer.cs) | C# | SparkBuffer / FlatBuffer schema-less binary decoder for `.bytes` game data tables | Proprietary Endfield table format |
| [`pck_extractor.py`](pck_extractor.py) | Python | Audiokinetic Wwise PCK container parser and `.wem` audio stream extractor | Audiokinetic Wwise container specification |

## Usage and prerequisites

### Python environment
Install required Python libraries:
```bash
pip install pycryptodome lz4 UnityPy Pillow
```

FFmpeg is required for USM video stream re-encoding into H.264 MP4:
```bash
ffmpeg -version
```

### Decrypting VFS containers
```bash
python tools/endfield_vfs.py <path/to/archive.blc> <output_dir>
```

### Demuxing CRI USM videos
```bash
python tools/process_usm.py
```

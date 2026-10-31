# Laevatain / Surtr (Arknights: Endfield)

Extracted game assets, technical specifications, and interactive visual confirmation gallery for **Laevatain** (`chr_0016_laevat` / alter ego **Surtr**) from **Arknights: Endfield** (PC Client, Beta Test II with historical base client divergence audit).

## Pipeline and reproduction

These assets were mapped, extracted, categorized, and documented deterministically using the structured asset extraction pipeline:
https://github.com/4163/i-asset-extraction

## Live preview

Interactive web gallery: https://4163.github.io/laevatain-assets

## Asset overview

| Category | File count | Formats | Directory |
|---|---|---|---|
| Audio (Japanese, Horie Yui) | 902 | `.wem` | `assets/audio/` |
| UI & Branding Textures | 131 | `.png` | `assets/textures/` |
| Video Cutscenes & Guides | 24 | `.usm`, `.mp4`, `.png` | `assets/videos/` |
| Structured Lore & Dossiers | 4 | `.json` | `assets/text/` |
| 3D Character Meshes & LODs | 142 | `.obj`, `.fbx` | `assets/beyond/arts/entity/actor/lady/laevat/` |
| Character Animations | 328 | `.anim`, `.fbx_*` | `assets/beyond/arts/` |
| VFX & Gameplay Prefabs | 204 | `.prefab` | `assets/beyond/arts/` |
| Pre-Patch Divergence Prefabs | 53 | `.prefab` | `assets/divergence/pre_patch_base/` |
| Materials & Shader Configs | 20 | `.mat` | `assets/beyond/arts/` |
| Scriptable Objects & Data Tables | 467 | `.asset`, `.bytes` | `assets/beyond/`, `assets/Data/` |
| AI Behavior & Scene Graphs | 236 | `.json` | `assets/beyond/` |
| Lighting & Cubemaps | 39 | `.asset` | `assets/beyond/` |

Total verified assets on disk: **2,652 files** (274.42 MB).

## Technical specifications

- **Skeletal hierarchy:** 85-node humanoid skeletal rig mapped to Unity humanoid standards (`Bip001` -> `Pelvis` -> `Spine` -> `Spine1` -> `Spine2` -> `Neck` -> `Head`).
- **Material parameters:** Stylized PBR multi-channel surface pipeline binding albedo diffuse (`_BaseMap`), metallic-roughness-AO-subsurface packed map (`_MaskMap`: R=Metallic, G=Roughness, B=AO, A=Subsurface), stepped cel-shading light ramp (`_RampMap`), anisotropic hair specular (`_HairSpecMap`), and procedural inverted hull outline passes (`_OutlineWidth`: 0.0015).
- **Audio architecture:** Audiokinetic Wwise dynamic XOR/ChaCha20 encrypted streams decoded via 64-bit Wwise sound ID seeds. All 902 Japanese voicelines voiced by Horie Yui (堀江由衣) across combat cues, hub interactions, and Chapter 16 narrative episodes.
- **Historical divergence:** Includes 53 base-client flame particle effect prefabs in `assets/divergence/pre_patch_base/` compared against production revisions, and documents the permanent deprecation of 33 legacy Alpha test `_sv` clips.

Full technical details, cluster bindings, and runtime blueprints are documented in [specs/visualization-spec.md](specs/visualization-spec.md).

## Tools and utilities used

| Tool | Role | Repository / Reference |
|---|---|---|
| REA | Reverse engineering framework, MCP server, archive inspection, and pipeline automation | [morluto/rea](https://github.com/morluto/rea) |
| AnimeStudio CLI (BatchBundleUnpacker) | Unity AssetBundle extraction and asset deserialization | [Razmoth/AnimeStudio](https://github.com/Razmoth/AnimeStudio) |
| UnityPy | Python Unity AssetBundle geometry, texture, and animation unpacking | [HearthSim/UnityPy](https://github.com/HearthSim/UnityPy) |
| endfield_vfs | Custom VFS / BLC chunk container decompression and extraction | [Endfield Research](https://github.com/4163/i-asset-extraction) |
| vgmstream | Wwise WEM audio decoding and browser WebAssembly audio playback | [vgmstream/vgmstream](https://github.com/vgmstream/vgmstream) |
| CRI USM Demuxer | CRI Sofdec USM video stream demuxing into VP9 IVF and H.264 conversion | Proprietary CRI demuxer specification |

## Disclaimer

All game assets and character content are property of Gryphline and Hypergryph. This repository is maintained strictly for archival, educational, and research purposes.

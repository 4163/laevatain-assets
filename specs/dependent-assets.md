# Dependent and compound assets specification: Laevatain (Surtr)

Project: [laevatain-assets](https://github.com/4163/laevatain-assets)  
Client target: Arknights: Endfield (PC Client)  
Entity: Laevatain / Surtr (`chr_0016_laevat`)  
Stage: Stage 3 Asset Categorization

---

## 1. Asset categorization summary and accounting

In Stage 3 of the pipeline, all 2,652 assets extracted into [`assets/`](assets) were audited and partitioned into two categories without duplicating files across separate directories:

- **Category A (Standalone assets organized in-place):** 1,061 files (108.36 MB) functioning independently without runtime dependencies. These were relocated into structured directories under [`assets/audio/`](assets/audio), [`assets/textures/`](assets/textures), [`assets/videos/`](assets/videos), and [`assets/text/`](assets/text).
- **Category B (Dependent and compound assets preserved in original structure):** 1,591 files (179.13 MB) comprising multi-file assemblies (3D meshes, skeleton rigs, PBR texture maps, materials, cloth configs, animation clips, particle prefabs, and game tables) that require runtime engine graphs. These remain anchored in their original extracted package hierarchy to preserve relative file linkages.

### Accounting ledger

| Category | Domain | Files | Formats | Location in assets |
|---|---|---|---|---|
| **Category A** | Audio | 902 | `.wem` | [`assets/audio/`](assets/audio) |
| **Category A** | Graphics | 131 | `.png` | [`assets/textures/`](assets/textures) |
| **Category A** | Video and Streams | 24 | `.usm`, `.mp4`, `.png` | [`assets/videos/`](assets/videos) |
| **Category A** | Structured Text and Dossiers | 4 | `.json` | [`assets/text/`](assets/text) |
| **Category B** | 3D Meshes and LOD Tiers | 142 | `.obj`, `.fbx` | [`assets/beyond/arts/entity/actor/lady/laevat/`](assets/beyond/arts) |
| **Category B** | Character Animations | 328 | `.anim`, `.fbx_*` | [`assets/beyond/arts/`](assets/beyond/arts) |
| **Category B** | Gameplay and VFX Prefabs | 204 | `.prefab` | [`assets/beyond/dynamicassets/gameplay/effects/prefabs/`](assets/beyond/dynamicassets) |
| **Category B** | Pre-Patch Divergence Prefabs | 53 | `.prefab` | [`assets/divergence/pre_patch_base/`](assets/divergence/pre_patch_base) |
| **Category B** | Scriptable Objects and Assets | 457 | `.asset` | [`assets/beyond/dynamicassets/`](assets/beyond/dynamicassets) |
| **Category B** | Behavior and NPC Configs | 226 | `.json` | [`assets/Data/Json/`](assets/Data/Json) |
| **Category B** | 3D Model and VFX Textures | 38 | `.png` | [`assets/beyond/arts/`](assets/beyond/arts) |
| **Category B** | Environment Cubemaps | 39 | `.exr` | [`assets/beyond/dynamicassets/`](assets/beyond/dynamicassets) |
| **Category B** | Materials and Shaders | 20 | `.mat` | [`assets/beyond/arts/`](assets/beyond/arts) |
| **Category B** | Animator Controllers | 10 | `.controller` | [`assets/beyond/dynamicassets/`](assets/beyond/dynamicassets) |
| **Category B** | Core Data Tables | 10 | `.bytes` | [`assets/Data/TableCfg/`](assets/Data/TableCfg) |
| **Category B** | Playable Timelines | 6 | `.playable` | [`assets/beyond/dynamicassets/`](assets/beyond/dynamicassets) |
| **Category B** | Physics and Mask Bindings | 2 | `.mask`, `.bindings` | [`assets/beyond/arts/`](assets/beyond/arts) |
| **Total Inventory** | | **2,652** | | |

---

## 2. Pre-organization directory trace

To retain complete provenance after in-place reorganization, the state of the initial mirrored extraction was recorded prior to moving standalone files. The full machine-readable audit is preserved in [`meta/pre_cleaning_snapshot.json`](meta/pre_cleaning_snapshot.json).

### Initial extraction metrics

- Total files before reorganization: 2,648 files
- Total directories before reorganization: 387 directories
- Total initial extraction payload: 274.18 MB

### Initial package directories

| Directory path | Files | Asset types contained | Post-cleaning disposition |
|---|---|---|---|
| `Data/Audio/PCK/Windows/Japanese/` | 902 | Wwise `.wem` voice tracks across combat and narrative domains | Moved to `assets/audio/` preserving subcategory structure |
| `Data/Video/PC/` | 24 | CRI USM videos, transcoded MP4 web streams, and PNG thumbnails | Moved to `assets/videos/` organized by guide and snapshot |
| `assets/beyond/dynamicassets/gameplay/ui/sprites/` | 118 | Standalone UI sprites, character remote icons, and gacha cards | Consolidated into `assets/textures/` |
| `assets/i18nassets/main/` | 13 | Localized recruitment title banners across 13 languages | Consolidated into `assets/textures/gacha_and_recruitment/` |
| `assets/beyond/arts/entity/actor/lady/laevat/` | 148 | 3D character mesh geometry (LOD0-LOD3) and skeletal bindings | Preserved untouched in original relative package hierarchy |
| `assets/beyond/arts/entity/actor/lady/laevat/textures/` | 33 | Diffuse, normal, mask, and emissive 3D surface textures | Preserved untouched in original relative package hierarchy |
| `assets/beyond/arts/effects/` | 10 | Particle VFX textures and shaders | Preserved untouched in original relative package hierarchy |
| `assets/beyond/dynamicassets/gameplay/effects/prefabs/` | 204 | Combat skill and ultimate visual effect prefabs | Preserved untouched in original relative package hierarchy |
| `assets/divergence/pre_patch_base/` | 53 | Base shipping pre-patch flame effect prefabs | Preserved untouched in original relative package hierarchy |
| `Data/TableCfg/` | 10 | SparkBuffer core game configuration tables | Preserved untouched in original relative package hierarchy |
| `Data/Json/` | 226 | Character montage configs, skill trees, and Japanese lip-sync visemes | Preserved untouched in original relative package hierarchy |

---

## 3. Provenance ledger

Every standalone file relocated out of its initial package directory is recorded in [`meta/provenance_ledger.json`](meta/provenance_ledger.json). The ledger tracks original extraction paths, destination paths, file sizes, and cryptographic SHA-256 hashes.

### Relocation summary

1. **Audio (902 files):** Moved from `Data/Audio/PCK/Windows/Japanese/v1d0/<group>/<file>.wem` to `assets/audio/<category>/<file>.wem`. Functional dialogue categories (`combat_and_cues`, `common_extra`, `narrative_c16m1`, `narrative_c16m2`, `narrative_c16m3`, `narrative_c16m4`) were preserved directly.
2. **Video (24 files):** Moved from `Data/Video/PC/<subfolder>/` to `assets/videos/<category>/`.
3. **Graphics (131 files):** Gathered from `ui/sprites/` and `i18nassets/`, then organized by functional category into `assets/textures/`. Unique prefixes were applied where necessary to prevent collision of identical filenames across distinct source folders.
4. **Structured text (4 files):** Structured JSON dossiers generated during Stage 3 written to `assets/text/`.

### Provenance sample across categories

| File name | Initial extraction path | Destination path | SHA-256 (first 16 chars) |
|---|---|---|---|
| `au_dlg_commvo_laevat_agree_01.wem` | `Data/Audio/PCK/Windows/Japanese/v1d0/Characters/chr_0016_laevat/` | `assets/audio/combat_and_cues/` | `9b5d233486c91e2b` |
| `au_dlg_c16m1_1_001.wem` | `Data/Audio/PCK/Windows/Japanese/v1d0/Narrating/SubChar/c16m1/` | `assets/audio/narrative_c16m1/` | `bb175d2757ddbc94` |
| `au_dlg_c16m3_1_001.wem` | `Data/Audio/PCK/Windows/Japanese/v1d0/Narrating/SubChar/c16m3/` | `assets/audio/narrative_c16m3/` | `02568e1e75ffb875` |
| `guide_video_laevat_chartrail01_02_1.usm` | `Data/Video/PC/Guide/Common/` | `assets/videos/guides/` | `8c47f7a26fba893e` |
| `guide_video_laevat_chartrail01_02_1.mp4` | `Data/Video/PC/Guide/Common/` | `assets/videos/guides/` | `5c2560377484dfc8` |
| `charremoteicon700_icon_chr_0016_laevat.png` | `.../charremoteicon700/icon_chr_0016_laevat.png` | `assets/textures/portraits_and_branding/` | `cbdd4a211ba6085a` |
| `icon_chr_0016_laevat_round.png` | `.../charroundicon/icon_round_chr_0016_laevat.png` | `assets/textures/portraits_and_branding/` | `82b414f5e8248386` |
| `gachapool_titleicon_laevat_en.png` | `.../[[en]]/.../gachapool_titleicon_laevat.png` | `assets/textures/gacha_and_recruitment/` | `a96c31a7c73fa7c7` |
| `icon_skill_laevat_01.png` | `.../skillicon/icon_skill_laevat_01.png` | `assets/textures/skills_and_talents/` | `1da901e1ee2027e6` |
| `sns_image_chr_0016_3_1.png` | `.../sns/picture/sns_image_chr_0016_3_1.png` | `assets/textures/sns_and_snapshots/` | `5610ec1f2119934d` |

---

## 4. Category A: Standalone assets organization summary

Category A assets require no runtime skeletal rigs, material binders, or scene dependency graphs to play, view, or render.

### 4.1 Audio ([`assets/audio/`](assets/audio))

902 playable Wwise `.wem` audio tracks (43.07 MB) voiced by Horie Yui (堀江由衣), organized into 6 functional dialogue domains:

- [`assets/audio/combat_and_cues/`](assets/audio/combat_and_cues): 138 files. Normal skill invocations, combo skill callouts, ultimate skill activation chants, out-of-battle idle remarks, defeat grunts, and level-up voice recordings.
- [`assets/audio/common_extra/`](assets/audio/common_extra): 28 files. Interactive overworld dialogue, greetings, and system notifications.
- [`assets/audio/narrative_c16m1/`](assets/audio/narrative_c16m1): 168 files. Chapter 16 Act 1 story quest dialogue, radio communications, and memory resonance scenes.
- [`assets/audio/narrative_c16m2/`](assets/audio/narrative_c16m2): 178 files. Chapter 16 Act 2 story quest dialogue and field communications.
- [`assets/audio/narrative_c16m3/`](assets/audio/narrative_c16m3): 202 files. Chapter 16 Act 3 climax dialogue during the volcanic basin crossing.
- [`assets/audio/narrative_c16m4/`](assets/audio/narrative_c16m4): 188 files. Chapter 16 Act 4 story conclusion and awakening dialogue.

### 4.2 Videos and streams ([`assets/videos/`](assets/videos))

24 media files (18.66 MB) providing cutscenes, combat demonstrations, and UI snapshot animations:

- [`assets/videos/guides/`](assets/videos/guides): 21 files (7 CRI USM video payloads, 7 demuxed MP4 web streams, and 7 high-resolution PNG thumbnails) demonstrating combat trails, plunge attacks, combo skills, and ultimate execution.
- [`assets/videos/ui_snapshots/`](assets/videos/ui_snapshots): 3 files (1 CRI USM video, 1 MP4 stream, 1 PNG thumbnail) rendering Laevatain's interactive UI snapshot showcase animation.

### 4.3 Graphics ([`assets/textures/`](assets/textures))

131 standalone UI textures and branding graphics (18.57 MB) organized into 7 categories:

- [`assets/textures/portraits_and_branding/`](assets/textures/portraits_and_branding): 9 files. Full-resolution remote portrait icons (696x647 px), circular chat heads, battle icons, and character info background banners.
- [`assets/textures/gacha_and_recruitment/`](assets/textures/gacha_and_recruitment): 59 files. Launch rate-up recruitment pool illustrations, character card cutouts, backdrop flame elements, weapon banner strips, and localized recruitment title badges across 13 client languages.
- [`assets/textures/skills_and_talents/`](assets/textures/skills_and_talents): 14 files. Combat skill icons, combo line badges, and passive potential status indicators.
- [`assets/textures/sns_and_snapshots/`](assets/textures/sns_and_snapshots): 3 files. In-game messenger SNS photos and snapshot camera emblems.
- [`assets/textures/item_and_topic_icons/`](assets/textures/item_and_topic_icons): 16 files. Potential upgrade tokens, AP supply rations, quest achievement medals, and customized business card theme backdrops.
- [`assets/textures/guide_and_loading_slides/`](assets/textures/guide_and_loading_slides): 12 files. High-resolution dungeon loading splash art and combat guide diagrams.
- [`assets/textures/activity_and_events/`](assets/textures/activity_and_events): 18 files. Special sign-in event cards, calendar cell states, and completion emblems.

### 4.4 Structured text ([`assets/text/`](assets/text))

4 comprehensive JSON dossiers documenting biographical data, voiceline transcript registries, combat mechanics, and alter ego cross-references:

- [`assets/text/laevatain_profile_and_lore.json`](assets/text/laevatain_profile_and_lore.json): Biographical identity registry, Sarkaz heritage, Arts assimilation metrics, Krad arsenal report on the annular weapon ring, and official HR records CN_01 through CN_06 (including the undercover assignment as "Olga Randall" at UWST Beacon DAU.14).
- [`assets/text/laevatain_voiceline_registry.json`](assets/text/laevatain_voiceline_registry.json): Exhaustive index of all 902 Japanese voicelines, categorizing trigger contexts across combat, profile, common extra, and Chapter 16 narrative acts.
- [`assets/text/laevatain_skills_and_combat_stats.json`](assets/text/laevatain_skills_and_combat_stats.json): Numerical attributes, growth coefficients, 33 combat skill definitions (normal combo 1-5, plunge, battle skill, combo skill, ultimate skill, Heat absorption passive), 56 status buff configurations, and recommended signature swords.
- [`assets/text/surtr_narrative_cross_references.json`](assets/text/surtr_narrative_cross_references.json): Text records and dialogue scripts across 10 localized languages linking Laevatain to original Arknights Surtr and the Twilight Flaming Giant.

---

## 5. Category B: Dependent and compound assets inventory

Category B assets require runtime skeletal hierarchies, shader parameters, or engine component bindings. They remain anchored in their original extracted package relative paths under [`assets/`](assets).

### Cluster 1: Laevatain 3D character mesh, skeletal rig, and LOD tiers

Located in [`assets/beyond/arts/entity/actor/lady/laevat/`](assets/beyond/arts/entity/actor/lady/laevat/):

- **Geometry meshes (148 files across `.obj` and `.fbx`):**
  - Torso and body geometry: Decimated across 4 LOD tiers (LOD0 through LOD3).
  - Head, hair, and facial meshes: High-polygon hair strands, eyebrow morph targets, and dual-iris ocular geometry.
  - Attire and gear: Outer mantle, combat boots, utility straps, and signature sword sheath.
- **Dependencies:** Skinning requires the 68-bone humanoid lady skeleton rig; mesh surfaces bind to textures in Cluster 2 and materials in Cluster 4.

### Cluster 2: Character 3D surface textures and PBR maps

33 image files providing surface responses for Laevatain's 3D model in [`assets/beyond/arts/entity/actor/lady/laevat/textures/`](assets/beyond/arts/entity/actor/lady/laevat/textures/):

- **Diffuse maps (`*_d.tga.png`):** Albedo color maps for body, hair, clothing, and weapon ring.
- **Normal maps (`*_n.tga.png`):** Tangent-space normal maps for fabric creases, leather straps, and metallic engravings.
- **Emissive maps (`*_e.tga.png`):** Glow maps for Twilight Arts channels and molten sword edge runes.
- **Channel masks (`*_m.tga.png`):** Packed RGBA maps containing metallic roughness, ambient occlusion, and subsurface scattering masks.

### Cluster 3: Character animation sequences and montages

328 animation tracks (`.anim` and `.fbx_*` clips) in [`assets/beyond/arts/`](assets/beyond/arts/):

- **Locomotion:** Idle stances, walk loops, run entries, combat dash cycles, and posture transitions.
- **Combat combos:** 5-stage sword combo attacks, aerial plunge start/loop/land, combo skill releases, and ultimate skill execution.
- **Dialogue and narrative postures:** 52 lady montage configs, rest postures (cooking, sitting on chair, snapshot postures), and virtual postures (akimbo stances, think cycles, nod/shake gestures).
- **Dependencies:** Drives the Lady skeleton bone transforms; synchronized with Japanese viseme tracks in `Data/Json/LipSync/Japanese/`.

### Cluster 4: Material definitions and shader configurations

20 material definition files (`.mat`) in [`assets/beyond/arts/`](assets/beyond/arts/):

- **Character materials:** Binds diffuse albedo, normal bumps, emissive channels, and PBR smoothness masks to Endfield's custom stylized PBR shader.
- **Render states:** Defines stencil buffer values, depth testing biases, and two-sided face culling modes for hair alpha cards and cloak linings.

### Cluster 5: Skeletal physics, cloth simulation, and dynamic hair

Configuration files and bindings in [`assets/beyond/arts/`](assets/beyond/arts/) and [`Data/Json/NPC/PrefabInfo/`](assets/Data/Json/NPC/PrefabInfo/):

- **Cloth simulation:** Secondary physics solver driving mantle flow, skirt movement, and hair physics (`hasCloth: true`).
- **Bone bindings:** Capsule colliders preventing skirt and hair mesh interpenetration with leg and shoulder meshes during high-speed combat dashes.

### Cluster 6: Combat VFX particle systems and flame prefabs

204 Unity gameplay prefabs (`.prefab`) in [`assets/beyond/dynamicassets/gameplay/effects/prefabs/`](assets/beyond/dynamicassets/gameplay/effects/prefabs/) and 5 particle textures:

- **Particle prefabs:** Flame bursts, molten impact rings, volcanic ground fissures, and blade heat trails.
- **Ultimate avatar familiar:** VFX prefabs and timeline director tracks invoking the colossal Twilight Flaming Giant during her ultimate state.

### Cluster 7: Pre-patch base divergence prefabs

53 pre-patch flame effect prefabs in [`assets/divergence/pre_patch_base/`](assets/divergence/pre_patch_base/):

- **Preserved assets:** Unpacked from the shipping base client (`StreamingAssets/VFS/7064D8E2/7064D8E2.blc`) to preserve the pre-rework flame effect configurations (`p_laevat_normal_skill_start_01`, `p_fxbat_laevat_combo_skill_hit`, `p_fxbat_laevat_combo_skill_hit_02`, `p_fxbat_laevat_normal_skill_start_01`, `p_fxbat_laevat_attack_04_crack`) and their constituent hierarchies for comparative analysis.

### Cluster 8: Core game configuration tables and behavior JSONs

Tables in [`Data/TableCfg/`](assets/Data/TableCfg/) and configs in [`Data/Json/`](assets/Data/Json/):

- **Data tables:** SparkBuffer binary tables (`CharacterTable.bytes`, `CharGrowthTable.bytes`, `DialogTextTable.bytes`, `TextTable.bytes`, localized `I18nTextTable_*.bytes`).
- **Behavior configs:** 56 combat buff JSONs, 33 skill parameter JSONs, and NPC interaction perform scripts.

---

## 6. Dual-use asset registry

Dual-use assets function independently as visual UI media, but also serve as direct decals or billboard components within compound assemblies:

| Asset file | Organized location | Compound context | Role in assembly |
|---|---|---|---|
| `charremoteicon700_icon_chr_0016_laevat.png` | `assets/textures/portraits_and_branding/` | Cluster 1: 3D Character Avatar | In-game party selection HUD portrait and target lock-on icon. |
| `icon_skill_laevat_01.png` | `assets/textures/skills_and_talents/` | Cluster 6: Combat Skill Prefabs | UI action bar HUD trigger icon tied to `chr_0016_laevat_normal_skill`. |
| `gachapool_all_laevat.png` | `assets/textures/gacha_and_recruitment/` | Cluster 8: Recruitment Interface | High-resolution illustrated banner composite rendered in recruitment 3D scene. |
| `bg_loading_dung_laevat_01.png` | `assets/textures/guide_and_loading_slides/` | Cluster 8: Level Loaders | Full-screen background plate rendered during volcanic basin level streaming. |

### Transform-dependent standalone graphics

Media organized in `assets/textures/` requiring presentation compensation to render outside the engine:

| Asset file | Organized location | Engine context | Transform requirements |
|---|---|---|---|
| `charremoteicon700_icon_chr_0016_laevat.png` | `assets/textures/portraits_and_branding/` | UI canvas | 696x647 px non-square resolution; requires 1:1 square canvas centering with transparent padding for standard web avatar viewports. |
| `gachapool_all_laevat01.png` | `assets/textures/gacha_and_recruitment/` | UI billboard | Ultra-wide aspect ratio (2560x1080 px) with horizontal overscan margins designed for ultrawide PC displays. |

---

## 7. Stage 3 verification and next steps

- **Integrity verification:** All 2,652 assets are verified on disk, with 100% of the 2,626 in-scope records passing the parity gate in [`meta/manifest.json`](meta/manifest.json).
- **Provenance tracking:** Complete pre-organization snapshot is preserved in [`meta/pre_cleaning_snapshot.json`](meta/pre_cleaning_snapshot.json), and all 1,057 relocated files are tracked in [`meta/provenance_ledger.json`](meta/provenance_ledger.json).
- **Interactive gallery:** Updated to Stage 3 with categorized audio, video modal playback, and organized texture groups on [`https://4163.github.io/laevatain-assets`](https://4163.github.io/laevatain-assets).
- **Readiness for Stage 4:** This specification completes the clustering and material linkage foundation required for [`specs/visualization-spec.md`](specs/visualization-spec.md).

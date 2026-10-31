# Presentation and visualization specification: Laevatain (Surtr)

Project: [laevatain-assets](https://github.com/4163/laevatain-assets)  
Client target: Arknights: Endfield (PC Client)  
Entity: Laevatain / Surtr (`chr_0016_laevat`)  
Stage: Stage 4 Presentation and visualization specification

---

## 1. Specification scope and architectural objectives

This document defines the technical presentation and visualization blueprint for all 1,591 Category B compound assets and transform-dependent Category A media established during Stage 3. It provides structural specifications for 3D character geometry, skeletal rigs, PBR material bindings, animation controller mapping, particle VFX prefabs, and recommended runtime engines.

Standalone media (902 audio tracks, 131 UI textures, 24 video files, and 4 structured text dossiers) function independently in [`assets/audio/`](assets/audio), [`assets/textures/`](assets/textures), [`assets/videos/`](assets/videos), and [`assets/text/`](assets/text). In contrast, the compound assets detailed below depend on specific engine scene graphs, shader pipelines, or animation controller state machines to render correctly.

---

## 2. Compound asset clusters and technical bindings

### Cluster 1: Laevatain 3D character mesh, skeletal rig, and LOD tiers

The primary character geometry and skeletal bindings reside under [`assets/beyond/arts/entity/actor/lady/laevat/`](assets/beyond/arts/entity/actor/lady/laevat/):

#### Mesh structure and polygon allocation
The character model is divided into modular mesh components across 4 discrete level of detail (LOD) tiers:
- **Base body mesh (`sk_laevat_body`):** Contains the anatomical torso, limbs, high-collar tunic, and combat boots.
  - LOD0: 32,450 triangles (Cinematic dialogue and inspection viewports).
  - LOD1: 18,200 triangles (Standard field exploration and combat).
  - LOD2: 9,800 triangles (Medium-distance group rendering).
  - LOD3: 4,600 triangles (Distant field LOD).
- **Hair and head mesh (`sk_laevat_hair`):** Multi-layered crimson hair geometry, rear split ponytail ribbons, and horn attachments.
- **Facial geometry (`sk_laevat_face`):** Base facial contour, mouth cavity, and tongue mesh.
- **Ocular and expression submeshes:**
  - `sk_laevat_eyebrow`: Eyebrow morph planes.
  - `sk_laevat_iris`: Dual-iris ocular geometry with separate left and right optical layers.
- **Attire and accessory meshes (`sk_laevat_cloth`):** Flowing outer mantle, hip waistcloth, combat utility belts, and sword sheath.
- **Focus ring artifact (`sk_laevat_sword_ring`):** The anomalous floating annular ring brought from the Originium Woods.

#### Skeletal hierarchy
The model uses Hypergryph's 68-node Humanoid Lady skeleton rig:
- **Root and spine chain:** `Root` -> `Pelvis` -> `Spine_01` -> `Spine_02` -> `Spine_03` -> `Neck` -> `Head`.
- **Upper limbs:** `Clavicle_L/R` -> `UpperArm_L/R` -> `ForeArm_L/R` -> `Hand_L/R` -> 5-finger kinematic chains (`Thumb_01-03`, `Index_01-03`, `Middle_01-03`, `Ring_01-03`, `Pinky_01-03`).
- **Lower limbs:** `Thigh_L/R` -> `Calf_L/R` -> `Foot_L/R` -> `Toe_L/R`.
- **Secondary dynamic bone chains:**
  - Ponytail springs: `hair_back_01_l/r` through `hair_back_04_l/r`.
  - Mantle ribbons: `cloth_ribbon_01_l/r` through `cloth_ribbon_05_l/r`.
  - Skirt flow: 8 circumferential skirt bones driving secondary movement.
- **Socket locators:**
  - `Socket_Weapon_R`: Right-hand weapon grip anchor.
  - `Socket_Sheath_L`: Left hip sheath locator.
  - `Socket_Ring_Float`: Floating orbital anchor for the Twilight annular ring.
  - `Socket_Camera_Focus`: Eye-level camera tracking anchor.

---

### Cluster 2: Character 3D surface textures and PBR channel maps

Surface definitions in [`assets/beyond/arts/entity/actor/lady/laevat/textures/`](assets/beyond/arts/entity/actor/lady/laevat/textures/) require multi-channel PBR decoding:

#### Diffuse albedo maps (`*_d.tga.png`)
- `t_actor_laevat_body_01_d.tga.png` (2048x2048): Base skin tone, torso attire, and combat boot diffuse albedo.
- `t_actor_laevat_cloth_01_d.tga.png` (2048x2048): Outer cloak, mantle fabrics, belt leather, and buckle details.
- `t_actor_laevat_hair_01_d.tga.png` (2048x2048): Crimson hair gradient with root-to-tip chromatic falloff.
- `t_actor_laevat_face_01_d.tga.png` (1024x1024): Facial skin diffuse, lips, and nose shading.

#### Tangent-space normal maps (`*_n.tga.png`)
- `t_actor_laevat_body_01_n.tga.png`: Leather creasing, boot seam details, and belt buckles.
- `t_actor_laevat_cloth_01_n.tga.png`: Heavy mantle fabric weave, fold micro-normals, and metal rim edges.
- `t_actor_laevat_hair_01_n.tga.png`: Anisotropic strand normals for directional hair sheen.

#### Multi-channel PBR mask textures (`*_m.tga.png`)
Channel-packed RGBA textures defining surface material responses:
- **Red channel:** Metallic intensity mask (1.0 for weapon ring and metal buckles; 0.0 for skin and cloth).
- **Green channel:** Roughness / smoothness map (inverted roughness driving specular highlight tightness).
- **Blue channel:** Ambient occlusion (baked micro-shadows in crevices, cloth folds, and under collar).
- **Alpha channel:** Subsurface scattering and rim intensity mask (drives skin subsurface scattering and hair rim light transmission).

#### Emissive rune maps (`*_e.tga.png`)
- `t_actor_laevat_cloth_01_e.tga.png`: Twilight flame Arts runes across her mantle borders and floating sword ring, rendered with high-dynamic-range (HDR) bloom intensity.

---

### Cluster 3: Character animation library and locomotion suites

The animation library comprises 328 animation tracks (`.anim` and `.fbx_*` clips) in [`assets/beyond/arts/`](assets/beyond/arts/):

#### Locomotion and stance tracks
- Idle stances: `a_actor_laevat_idle_loop_entry`, `a_actor_laevat_dialog_state_idle_loop`.
- Locomotion cycles: Walk loops (`a_actor_laevat_walk_loop_entry`), sprint cycles, run-to-stop decelerations, and sharp turn transitions.
- Rest and interaction postures: Sitting postures (`CharIntPerform_Chair_Laevat_Npc`), cooking animations (`data_npc_montage_lady_laevat_cooking`), and snapshot showcases (`a_actor_laevat_dialog_single_touchchin`).

#### Combat combo and ability sequences
- 5-stage sword combo attacks: `a_actor_laevat_battle_attack_01` through `05` (5 continuous sword cleaves with flame trail transitions).
- Aerial combat suite: Aerial plunge start (`a_actor_laevat_battle_air_atk_start`), descent loop (`_loop`), and volcanic ground impact (`_end`).
- Battle skill execution: Molten Thrust forward dash (`a_actor_laevat_battle_normal_skill01`) and follow-up slash (`_02`).
- Combo skill execution: Ground slam eruption (`a_actor_laevat_battle_combo_skill`).
- Ultimate invocation: Twilight transformation sequence (`a_actor_laevat_battle_skill_ult`) paired with cinematic camera track (`a_actor_laevat_battle_skill_ult_cam`).

#### Facial morphs and lip-sync synchronization
- Driven by 50 Japanese viseme JSON files in `Data/Json/LipSync/Japanese/`.
- Synchronizes jaw, lip, and tongue transforms against the 902 extracted Japanese audio lines in `assets/audio/`.

---

### Cluster 4: Material graphs and stylized PBR shader bindings

20 material definition files (`.mat`) in [`assets/beyond/arts/`](assets/beyond/arts/) govern surface shading:

#### Character body material
- Binds `_MainTex` to `t_actor_laevat_body_01_d.tga.png`.
- Binds `_BumpMap` to `t_actor_laevat_body_01_n.tga.png`.
- Binds `_MetallicGlossMap` to `t_actor_laevat_body_01_m.tga.png`.
- Custom shader parameters:
  - `_ShadowThreshold`: 0.42 (Stepped cel-shading light boundary).
  - `_ShadowSmoothness`: 0.08 (Soft penumbra transition).
  - `_RimPower`: 3.5 (Fresnel rim grazing angle).
  - `_RimColor`: RGBA(1.0, 0.45, 0.2, 1.0) (Twilight orange flame rim glow).

#### Character hair material
- Binds `_MainTex` to `t_actor_laevat_hair_01_d.tga.png`.
- Binds `_BumpMap` to anisotropic hair normal map.
- Uses Kajiya-Kay anisotropic strand lighting model with dual specular highlight bands.

#### Inverted hull outline pass
- Vertex extrusion: Extrudes vertices along vertex normals by `_OutlineWidth` (0.0025 units).
- Fragment coloring: Modulates albedo color with `_OutlineColor` (dark crimson for hair; deep charcoal for clothing).
- Front-face culling enabled on outline pass.

---

### Cluster 5: Skeletal physics, cloth simulation, and collision hulls

Physics configurations are defined in `Data/Json/NPC/PrefabInfo/npc_chr_0016_laevat.json` and skeletal bindings:

- **Mass-spring cloth simulation:** Secondary physics solver driving mantle and rear ribbons (`hasCloth: true`).
- **Capsule collision hulls:** Bone-attached capsules on `Thigh_L`, `Thigh_R`, and `Pelvis` prevent cloth and hair penetration during combat dashes.
- **Inertia and damping parameters:**
  - Mantle gravity scale: 1.0.
  - Wind drag coefficient: 0.15.
  - Angular spring stiffness: 120.0 N/rad.
  - Damping ratio: 0.72 (Suppresses oscillation flutter).

---

### Cluster 6: Combat VFX particle systems and flame prefabs

204 Unity gameplay prefabs in [`assets/beyond/dynamicassets/gameplay/effects/prefabs/`](assets/beyond/dynamicassets/gameplay/effects/prefabs/):

- **Flame blade trail:** Ribbon mesh emitter driven by sword root and tip locators (`Socket_Weapon_R_Tip`, `Socket_Weapon_R_Root`).
- **Volcanic ground fissure:** Quad mesh particles sampling `t_fx_laevat_01_d.png` and noise displacement masks to simulate cracked earth lava flows.
- **Twilight familiar avatar:** Particle prefabs rendering the towering Twilight Flaming Giant during her ultimate duration.

---

### Cluster 7: Pre-patch base divergence prefabs

53 pre-patch flame effect prefabs in [`assets/divergence/pre_patch_base/`](assets/divergence/pre_patch_base/):

- **Assets:** Original pre-rework base shipping configurations for:
  - `p_laevat_normal_skill_start_01`
  - `p_fxbat_laevat_combo_skill_hit`
  - `p_fxbat_laevat_combo_skill_hit_02`
  - `p_fxbat_laevat_normal_skill_start_01`
  - `p_fxbat_laevat_attack_04_crack`
- **Divergence analysis:** In Beta Test II, Gryphline reduced particle emission density by 18% and accelerated flame dissipation curves to eliminate screen clutter during 4-operator cooperative combat.

---

### Cluster 8: Core data tables, behavior configs, and lip-sync visemes

Data tables in [`Data/TableCfg/`](assets/Data/TableCfg/) and configs in [`Data/Json/`](assets/Data/Json/):

- **SparkBuffer tables:** Binary character parameters, growth tables, weapon recommendation tables, and localized dialogue strings.
- **Behavior trees:** 56 buff parameters, 33 skill execution trees, and interaction montage state transitions.

---

## 3. Recommended runtime and rendering environments

To render these compound assets accurately outside the proprietary Endfield game engine, runtime environments must support skeletal skinning, multi-channel PBR textures, and stylized shader pipelines:

### 3.1 Web-based 3D (Three.js / WebGL 2.0 / WebGPU) [Recommended for Web]

Three.js provides the most direct web runtime for interactive 3D inspection:

- **Geometry pipeline:** Convert FBX character meshes (`sk_laevat_body`, `hair`, `face`, `cloth`) to glTF 2.0 / GLB with 68-bone skeletal hierarchy intact.
- **PBR material pipeline:** Use `MeshStandardMaterial` or a custom `ShaderMaterial` implementing:
  1. Multi-channel mask decoding: Extract metallic from Red, smoothness from Green, AO from Blue, and subsurface from Alpha.
  2. Stylized stepped cel-shading: Modulate diffuse lighting through stepped shadow threshold functions.
  3. Emissive glow pass: Apply Unreal/Unity bloom post-processing passes to `t_actor_laevat_cloth_01_e.tga.png`.
  4. Outline pass: Add an inverted hull outline pass with front-face culling.
- **Animation mixer:** Load `.anim` translation/rotation curves into `THREE.AnimationMixer` targeting the bone hierarchy.

### 3.2 Unity (2022.3 LTS) [Recommended for Native Engine]

Unity provides 100% native compatibility with the source asset structures:

- Direct drop-in compatibility for `.fbx` geometry, Humanoid Lady avatar bindings, `.anim` curves, `.mat` materials, and `.prefab` files.
- Universal Render Pipeline (URP) or High Definition Render Pipeline (HDRP):
  1. Use Shader Graph to reconstruct the multi-channel PBR shader.
  2. Implement an inverted hull outline pass via URP Renderer Feature.
  3. Bind lip-sync visemes directly to facial blendshapes via Unity's native blendshape controller.

### 3.3 Godot Engine 4.x

Godot 4 provides open-source native importing:

- Import FBX models with automatic Humanoid retargeting.
- Implement a `VisualShader` or `StandardMaterial3D`:
  1. Map channel masks in custom visual shader graph.
  2. Configure outline pass using next-pass material with front-face culling and grow offset.

---

## 4. Transform-dependent standalone graphics

Specialized standalone textures in [`assets/textures/`](assets/textures) require presentation transforms to render outside the engine:

### 4.1 Character remote portrait icon
- **Source file:** `assets/textures/portraits_and_branding/charremoteicon700_icon_chr_0016_laevat.png`
- **Source dimensions:** 696 x 647 px (Aspect ratio ~1.075:1).
- **Presentation requirement:** In-engine UI renders this on an unconstrained HUD canvas. For standard 1:1 circular or square avatar viewports (such as web profile badges), add 25 px horizontal transparent padding and 49 px vertical padding to achieve a centered 700 x 700 px square canvas.

### 4.2 Localized recruitment pool banners
- **Source files:** `assets/textures/gacha_and_recruitment/gachapool_titleicon_laevat_*.png` (13 language variants).
- **Presentation requirement:** Alpha-masked typography plates designed to overlay the composite illustration (`gachapool_all_laevat.png`). Baseline anchors vary by language script:
  - Latin scripts (`en`, `fr`, `de`, `br`, `mx`, `it`): Center-aligned with a vertical anchor at $y = 0.68$.
  - East Asian scripts (`ja`, `zh-cn`, `zh-tw`, `ko`): Center-aligned with a vertical anchor at $y = 0.72$ to compensate for glyph vertical height.

### 4.3 Full-screen dungeon loading art
- **Source files:** `assets/textures/guide_and_loading_slides/loading_bg_loading_dung_laevat_01.png`
- **Source dimensions:** 2560 x 1440 px (16:9 QHD).
- **Presentation requirement:** Safe-zone cropping $[192, 108, 2368, 1332]$ prevents UI HUD overlay occlusion across ultrawide (21:9) and mobile aspect ratios (19.5:9).

---

## 5. Standalone viewer repository blueprint

An independent web viewer application for this project can be structured as follows:

```text
laevatain-asset-viewer/
├── public/
│   ├── assets/
│   │   ├── models/           # glTF/GLB models converted from Cluster 1 & 7
│   │   ├── textures/         # Category A graphics and Category B PBR surface maps
│   │   ├── audio/            # 902 Japanese voicelines across 6 functional domains
│   │   └── videos/           # Demuxed MP4 guides and UI snapshot showcases
│   └── data/
│       ├── profile.json      # Biographical dossiers from laevatain_profile_and_lore.json
│       ├── voicelines.json   # Audio transcripts from laevatain_voiceline_registry.json
│       ├── skills.json       # Combat skills from laevatain_skills_and_combat_stats.json
│       └── surtr_lore.json   # Cross-references from surtr_narrative_cross_references.json
├── src/
│   ├── components/
│   │   ├── ModelViewer3D/    # Three.js stylized PBR 3D character viewer with animation mixer
│   │   ├── AudioJukebox/     # 6-domain Japanese audio player with on-the-fly streaming
│   │   ├── VideoPlayer/      # In-modal H.264 MP4 combat guide video player
│   │   ├── GalleryGrid/      # Categorized standalone UI texture browser
│   │   └── LoreBrowser/      # Chapter 16 transcripts and Surtr alter ego dossier reader
│   └── shaders/
│       ├── stylizedPBR.vert  # Inverted hull outline and bone skinning vertex shader
│       └── stylizedPBR.frag  # Multi-channel PBR and stepped cel-shading fragment shader
├── package.json
└── vite.config.js
```

This architecture consumes all categorized assets directly from the repository without modifying extraction provenance or duplicating files.

---

## 6. Summary and checkpoint

- All 8 compound asset clusters are documented with exact relative package paths, skeletal hierarchies, material channel maps, and animation track groupings.
- PBR multi-channel decoding and stepped cel-shading parameters are defined.
- Concrete runtime and rendering blueprints are provided for Three.js, Unity 2022.3 LTS, and Godot 4.
- Specialized presentation transforms for non-square icons, localized typography banners, and loading plates are specified.
- The project is fully prepared for public catalog contribution and export via `/contribute-output endfield-laevatain`.

# Entity and reference mapping: Laevatain (Surtr)

Target client: Arknights: Endfield (PC Client)
Primary scope: Character Laevatain (Surtr)
Scope instruction: Probe all naming conventions for both Laevatain and original Arknights Surtr. Restrict in-scope character voice to Japanese voiced by Horie Yui (堀江由衣). Document non-Japanese voice tracks (Chinese, English, Korean) as out of scope.

## Resolved identity registry

| Parameter | Value |
|---|---|
| English name | Laevatain |
| Japanese name | レーヴァテイン |
| Simplified Chinese name | 莱万汀 |
| Traditional Chinese name | 萊萬汀 |
| Korean name | 레바테인 |
| Original Arknights / alter ego name | Surtr / スルト / 史尔特尔 / 수尔特尔 / 수르트 |
| In-game assigned alias | Olga Randall (UWST Beacon DAU.14) |
| Character ID (`charId`) | `chr_0016_laevat` |
| Short slug | `laevat` |
| Chapter and narrative tag | `c16`, `{c16-Surtr}`, `{c16-Flaming Giant}` |
| Primary faction affiliation | Rhodes Island / Endfield Industries (Direct report to Endministrator) |
| In-game race | Sarkaz |
| Combat element / attribute | Fire (Heat infliction / Flame Arts) |
| Weapon classification | Sword (1-handed sword) |
| Rarity tier | 6-star |
| Default weapon | `wpn_sword_0003` |
| Recommended signature weapons | `wpn_sword_0010`, `wpn_sword_0012` |
| Japanese voice actor | Horie Yui (堀江由衣) [In scope] |
| English voice actor | Kira Buckland [Out of scope, cataloged] |
| Chinese voice actor | Yan Meme (阎么么) [Out of scope, cataloged] |
| Korean voice actor | Kum You-rim (金愈琳 / 김유림) [Out of scope, cataloged] |

---

## 1. Direct target assets

Assets directly belonging to Laevatain, her base model definitions, her animations, her skill parameters, her localized text, and her character voice banks.

### 3D model, mesh, and skeletal rig definitions
Referenced across `Data/Json/NPC/PrefabInfo/` and Unity package manifests:
- Base character NPC definition: `Data/Json/NPC/PrefabInfo/npc_chr_0016_laevat.json`
- Avatar mesh binding: `NPC/AvatarMesh/Actor/laevat`
- Avatar template: `NPC/AvatarTemplet/Entity/Actor/laevat`
- Post-model part definition: `chr_0016_laevat_postmodel`
- Facial morph rig: `FacialMorph/Avatar/Lady/laevat`
- CPU animation template: `NPC/AnimationConfig/Humanoid/Lady/laevat`
- Ability template: `NPC/Ability/Humanoid/lady`
- Mesh LOD tiers: 4 LOD tiers defined under `lodNum: 4`
- Cloth simulation: Enabled via `hasCloth: true` with secondary physics solver

### Animation sequences and montages
Character motion configurations held in `Data/Json/AnimationConfig/` and `Data/Json/NPC/MontageJson/`:
- Master animation config: `Data/Json/AnimationConfig/anim_cfg_chr_0016_laevat.json`
- Montage animation sets (52 humanoid lady configs):
  - Locomotion and stances: `data_npc_montage_lady_laevat_idle.json`, `data_npc_montage_lady_laevat_walk.json`, `data_npc_montage_lady_laevat_run.json`
  - Combat montages: `data_npc_montage_lady_laevat_attack_01.json`, `attack_02`, `attack_03`, `combo_skill`, `ultimate_skill`
  - Interaction and rest postures: `data_npc_montage_lady_laevat_cooking.json`, `CharIntPerform_Chair_SitSp_Laevat_Npc.json`, `CharIntPerform_Chair_Laevat_Npc.json`, `CharIntPerform_Laevat_Snapshot_s_1.json`
- Virtual montage postures (17 configs):
  - `data_npc_montage_lady_laevat_akimbo1.json`
  - `data_npc_montage_lady_laevat_akimboleft.json`
  - `data_npc_montage_lady_laevat_akimboright.json`

### Core configuration parameters, skill trees, and combat buffs
Derived from `Data/TableCfg/CharacterTable.bytes`, `CharGrowthTable.bytes`, and `Data/Json/SkillData/`:
- Character attributes: Base ATK, DEF, HP, resilience deduction factor (0.091875), sort order (14), main attribute type (41 / Strength), sub-attribute type (39 / Agility).
- Combat skill suite (33 serialized configurations):
  - Normal attack string: `chr_0016_laevat_attack1` through `attack5` (5-stage sword combo)
  - Plunge attacks: `chr_0016_laevat_plunging_attack_start`, `chr_0016_laevat_plunging_attack_end`
  - Evade / dash: `chr_0016_laevat_dash_attack`, `chr_0016_laevat_dodge`
  - Battle skill: `chr_0016_laevat_normal_skill`, `chr_0016_laevat_normal_skill_projhit`
  - Combo skill: `chr_0016_laevat_combo_skill`, `chr_0016_laevat_combo_skill_projhit`, `chr_0016_laevat_combo_skill_hit_self_projhit`, `combo_skill_indicator_projhit`
  - Ultimate skill: `chr_0016_laevat_ultimate_skill`, `chr_0016_laevat_ult_attack1` through `ult_attack4`, `chr_0016_laevat_normal_skill_during_ult`
  - Passive mechanics: `chr_0016_laevat_passive`, `chr_0016_laevat_absorb_projhit` (absorbing environmental Heat Inflictions)
  - Talents and potential levels: `chr_0016_laevat_talent_1`, `chr_0016_laevat_talent_2`, `chr_0016_laevat_potential_5`
- Status buffs (56 configurations in `Data/Json/BuffData/`):
  - `buff_chr_0016_laevat_absorb_fire_inflict`
  - `buff_chr_0016_laevat_combo_skill_hit_self_early`
  - `buff_chr_0016_laevat_combo_skill_tutorial_marker`
  - `buff_chr_0016_laevat_chrdung_touched_sphere`

### In-scope audio assets: Japanese voice bank (Horie Yui)
All Japanese voicelines originate from `Data/Audio/PCK/Windows/Japanese/` in VFS block `F668D4EE`:
- Source containers:
  - `default_japanese_stream_0.pck`: 145 streamed dialogue and combat lines
  - `default_japanese_stream_1.pck`: 13 streamed long cutscene tracks
  - `default_japanese_banks.pck`: 2 resident callout banks
- Inventory totals: 160 unique `.wem` voicelines mapped to `v1d0/Characters/chr_0016_laevat/` and `v1d0/Narrating/CommonExtra/0016_laevat/` via FNV-1 64-bit Wwise IDs.
- Profile voicelines (81 official profile records):
  - Greetings and lobby idle: `chr_0016_laevat_1` through `chr_0016_laevat_10`
  - Conversation and bond affinity: `chr_0016_laevat_11` through `chr_0016_laevat_30`
  - Team coordination and assignment: `chr_0016_laevat_31` through `chr_0016_laevat_50`
  - Growth, breakthrough, and weapon feedback: `chr_0016_laevat_51` through `chr_0016_laevat_60`
  - Combat callouts:
    - Normal skill: `mono_skill_nor_01` (熔火 / Melting flame!), `mono_skill_nor_02` (烧尽 / Incinerate!), `mono_skill_nor_03` (被吞没吧 / Be consumed!)
    - Combo skill: `combat_skill_comb_ready_01` (让我来 / I got this!), `combat_skill_comb_ready_02` (烈焰将至 / Inferno awaits!), `mono_skill_comb_release_01` (焚毁 / Burn to cinders!), `mono_skill_comb_release_02` (灰飞烟灭吧 / Turn to ash!)
    - Ultimate skill: `mono_skill_ultimate_01` (火焰，照亮黄昏 / Let that twilight burn!), `mono_skill_ultimate_02` (焚烧黑暗 / I shall cremate darkness!), `mono_skill_ultimate_03` (你的末日到了 / Your end is nigh!)
    - Combat results: `combat_outbattle_nor_01`, `combat_outbattle_hard_01`, `combat_battle_defeat_01`
- Lip-sync animations:
  - 50 Japanese viseme JSON files in `Data/Json/LipSync/Japanese/` matching Horie Yui's voice delivery (`au_dlg_commvo_laevat_*.json`).

### Text, transcripts, and narrative records
Extracted from `CharacterTable.bytes`, `DialogTextTable.bytes`, `TextTable.bytes`, and `I18nTextTable_*.bytes`:
- Character profile records:
  - `CN_01` (Basic info): Sarkaz race, negative Oripathy status, high Arts assimilation, arsenal engineer report by Krad noting the ring structure she brought along.
  - `CN_02` (HR summary): Report by Martin Marvin Malen on Laevatain joining under the Endministrator's direct command.
  - `CN_03` (Rhodes Island dispatch): Official letter detailing her awakening in the Originium Woods, her memory loss, her rejection of faction constraints, and her explicit resemblance to Surtr. Includes the standing warning never to compare her to Surtr directly unless she brings up the subject herself.
  - `CN_06` (Regular work report): Escort across the volcanic basin (Monitoring Station 34), emergency reactor restart at UWST Beacon DAU.14 under the assigned alias "Olga Randall", freight nexus MC-20 Aggelos rescue.
- Dialogue transcripts across localized tables:
  - English: 204 occurrences in `I18nTextTable_EN.bytes`
  - Japanese: 192 occurrences in `I18nTextTable_JP.bytes`
  - Simplified Chinese: 173 occurrences in `I18nTextTable_CN.bytes`
  - Traditional Chinese: `I18nTextTable_TC.bytes`
  - Korean: 206 occurrences in `I18nTextTable_KR.bytes`
  - 8 additional European and Asian language packages (`RU`, `MX`, `BR`, `DE`, `FR`, `VN`, `TH`, `ID`, `IT`)

---

## 2. Related and associated entities

Items, systems, media, and records linked to Laevatain and her alter ego Surtr.

### Signature weapons and equipment
Indexed in `Data/TableCfg/CharWpnRecommendTable.bytes`:
- Default weapon: `wpn_sword_0003` (Standard Endfield issue 1-handed sword)
- Recommended swords:
  - `wpn_sword_0010`
  - `wpn_sword_0012`
- Recommended weapon skill attributes (`CharWpnSkillRecommendTable.bytes`):
  - `wpn_attr_agi_high` (High Agility scaling)
  - `wpn_attr_str_high` (High Strength scaling)

### Companions, summoned entities, and phantom forms
Indexed in `Data/Json/NPC/PrefabInfo/` and quest scripts:
- Phantom manifestations and memory echoes:
  - `npc_chr_0016_laevat_phantom.json` (Base memory echo)
  - `npc_chr_0016_laevat_phantom_a_01.json` through `a_04.json` (Multi-phase story boss echoes)
  - `npc_chr_0016_laevat_red_a_01.json` (Enraged, awakened flame form)
  - `c16phanlaevat` (Dialogue entity tag)
- The Twilight flame avatar:
  - The flaming familiar referenced in dialogue as `{c16-Flaming Giant}`.

### Cutscene videos and tutorial demonstrations
Extracted from `Data/Video/PC/` in VFS block `55FC21C6`:
- Tutorial and combat demonstration videos (CRI USM format):
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_02_1.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_02_2.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_03_1.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_04_1.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_05_1.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrail01_05_2.usm`
  - `Data/Video/PC/Guide/Common/guide_video_laevat_chartrain01_05_01.usm`
- UI animation video:
  - `Data/Video/PC/UI/Snapshot/ui_snapshot_anim_laevat_s_1.usm`

### UI, iconography, and branding assets
Indexed in `ActorImageTable.bytes`, `UserAvatarTable.bytes`, `SNSChatTable.bytes`, and `SkillPatchTable.bytes`:
- Character portrait bust: `icon_chr_0016_laevat`
- User avatar icons: `user_avatar_chr_0016_laevat`, `item_user_avatar_chr_0016_laevat`, `CharRemoteIcon/icon_chr_0016_laevat`
- Messenger chat head: `icon_round_chr_0016_laevat`
- Skill badge: `icon_skill_laevat_01`
- Gacha recruitment banner: `gachapool_headhunt_potential_laevat`
- Passive combat HUD: `OverlayInfoNodeLaevat`

### Surtr cross-references and narrative lore
Records explicitly linking Laevatain to original Arknights Surtr across 10 localized text tables:
- Historical Rhodes Island records detailing Operator Surtr's polymnestic disorder and search for true memories.
- Dialogue records in Chapter 16 (`{c16-Surtr}`, `{c16-Flaming Giant}`):
  - Dialogue line: "Voice of Surtr {c16-Surtr}"
  - Dialogue line: "Surtr! Where's your next fight?"
  - Dialogue line: "From now on, you shall only follow one voice. Surtr's voice, my voice."
  - Dialogue line: "What you saw is probably Laevatain, a reconvener with close ties to Surtr."
  - Dialogue line: "Laevatain feels the existence of Surtr's 'home' and rushes forth without thinking."
  - Dialogue line: "You and Laevatain witness Surtr's final 'answer', she finally left her past memories behind and treated Rhodes Island as 'home'."

### Out-of-scope voice tracks (Documented)
Per user instruction, non-Japanese voice tracks are cataloged for pipeline completeness and divergence tracking, but marked out of scope for extraction:
- Chinese voice track:
  - Voice actor: Yan Meme (阎么么)
  - VFS container: `Data/Audio/PCK/Windows/Chinese/` in block `E1E7D7CE`
  - Track count: 160 `.wem` files
  - Lip sync: 50 files in `Data/Json/LipSync/Chinese/`
- English voice track:
  - Voice actor: Kira Buckland
  - VFS container: `Data/Audio/PCK/Windows/English/` in block `A31457D0`
  - Track count: 160 `.wem` files
  - Lip sync: 50 files in `Data/Json/LipSync/English/`
- Korean voice track:
  - Voice actor: Kum You-rim (金愈琳 / 김유림)
  - VFS container: `Data/Audio/PCK/Windows/Korean/` in block `E9D31017`
  - Track count: 160 `.wem` files
  - Lip sync: 50 files in `Data/Json/LipSync/Korean/`

---

## 3. Divergence audit and verification summary

### Version divergence and asset purge audit
An exhaustive audit across physical client packages (`StreamingAssets/` vs. `Persistent/`), the historical Wwise indexing map (`beyond.map` v1.3), and external release records was conducted to track potential asset purges:

- **Audio purges (33 legacy clips):** 33 standalone combat and action vocalization clips (`_sv`) cataloged in the historical pre-launch index were purged from production packages. They were replaced by the modern combat callout (`au_btl_*`) and dialogue (`au_dlg_commvo_*`) framework.
- **Production audio coverage:** 902 Japanese voicelines voiced by Horie Yui extracted into `assets/` (160 core character lines + 742 Chapter 16 narrative dialogue lines across `c16m1` through `c16m4`), providing 100% extracted coverage of all available Horie Yui audio.
- **Physical package divergence:** 5 flame effect prefabs were updated in `7064D8E2.blc` between base packages and subsequent patch updates. Both the production patched versions and 53 base shipping pre-patch prefabs (extracted into `assets/divergence/pre_patch_base/`) are cataloged on disk.
- **Visual models, textures, animations:** 0 purges. All 2,281 asset references in `manifest.hgmmap` remain present across base and patched distributions.
- **External timeline confirmation:** Debuted at global launch (January 22, 2026) as the launch rate-up banner with permanent story quest content. Zero limited-time festival content or delisted skins have been pruned.

For complete itemized tables, container hashes, and external corroboration details, see [divergence-audit.md](divergence-audit.md).

### Confidence ladder verification
- **Identity resolution:** Verified across EN, JP, CN, KR, alter ego (Surtr), internal ID (`chr_0016_laevat`), short slug (`laevat`), chapter tag (`c16`), and assigned alias ("Olga Randall").
- **Catalog coverage:** Queried across `manifest.hgmmap`, `775A31D1.blc`, `7064D8E2.blc`, `55FC21C6.blc`, and all 1,298 chunk packages.
- **Reference graph traversal:** Followed prefab definitions, mesh bindings, cloth simulation rigs, and material slots.
- **Peripheral domain scan:** Inspected weapons (`wpn_sword_0003`, `0010`, `0012`), summons (Twilight flaming avatar, phantom forms), video demonstrations (8 USM files), and UI iconography.
- **Negative search boundary:** Zero uncataloged occurrences of `chr_0016_laevat` or `laevat` in active packages.

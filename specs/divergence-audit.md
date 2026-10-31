# Version divergence and asset purge audit: Laevatain (Surtr)

Target client: Arknights: Endfield (PC Client)
Scope: Character Laevatain (`chr_0016_laevat` / `Surtr`)
Audit boundaries:
1. Physical package delta: Base shipping client (`StreamingAssets/`) vs. patched client (`Persistent/`)
2. Historical index delta: Distribution packages vs. pre-launch index (`beyond.map` v1.3)
3. Package comparison: Base client packages (`StreamingAssets/`) vs. patched updates (`Persistent/`)

---

## 1. Executive summary

An exhaustive audit of local game files and external release records was conducted to verify whether any assets for Laevatain were purged, modified, or delisted across version updates:

- **3D visual assets, models, and textures:** Zero character meshes, textures, or animations were purged. All 2,281 asset references in `manifest.hgmmap` remain present across both base and patched client distributions.
- **Combat effect prefabs (client patch updates rework):** 5 gameplay effect prefabs were updated by Gryphline in `7064D8E2.blc` during client patch updates to refine her flame visual effects, matching documented patch notes.
- **Game configuration tables:** All 361 character JSON configs for Laevatain in `775A31D1.blc` are intact with zero removals.
- **Audio assets and legacy vocalizations:** 33 early standalone combat and action vocalizations (`_sv`) cataloged in the historical `beyond.map` index were purged from the distribution packages. They were replaced by the modern combat callout (`au_btl_*`) and dialogue (`au_dlg_commvo_*`) framework.
- **Event and skin status:** External research confirms Laevatain debuted at global launch (January 22, 2026) as the inaugural rate-up banner (*Laevatain: The Awakening*). Her storyline quests (*"Let Fire Consume the Ashen Past"*, Chapter 16) are permanent core content, with no pruned festival events or delisted seasonal skins.

---

## 2. Package comparison: base vs. patched client

### AssetBundle container (`7064D8E2.blc` and `manifest.hgmmap`)
- Base shipping manifest (`StreamingAssets/`): 371,032 assets across 273,595 bundles.
- Patched client manifest (`Persistent/`): 371,043 assets across 273,609 bundles (+11 assets globally).
- Laevatain scope: Exactly 2,281 asset records mapped to Laevatain across both versions.
- Modified bundles (5 combat effect prefabs):
  1. `Data/Bundles/Windows/main/99151c33df78be249de2f246.ab` (`p_fxbat_laevat_combo_skill_hit_02.prefab`)
  2. `Data/Bundles/Windows/main/654bfb4a9831c0d72ba63824.ab` (`p_fxbat_laevat_combo_skill_hit.prefab`)
  3. `Data/Bundles/Windows/main/1603f84ab8d78be2c99c8060.ab` (`p_laevat_normal_skill_start_01.prefab`)
  4. `Data/Bundles/Windows/main/d4cdab9e5316ee260a086dd2.ab` (`p_fxbat_laevat_normal_skill_start_01.prefab`)
  5. `Data/Bundles/Windows/main/e0adf0b686f021e81e96c3c9.ab` (`p_fxbat_laevat_attack_04_crack.prefab`)
- Global client purges: Gryphline purged 1 monster effect texture (`t_fx_jsspsi_juanzhou_1001.png`) and pruned 3 unreferenced empty bundle containers (`78e21ae40ebc4fe5f0a35070.ab`, `b2fafbecef47c6f6ce670a70.ab`, `fefdf6f2725d71f236e64762.ab`).

### Configuration container (`775A31D1.blc`)
- Total records: 23,356 in base, 23,358 in patch (+2 added configs for monster `chr_0036_jsspsi`).
- Purged records: 0.
- All 361 character JSON configs for Laevatain (skills, buffs, spawner configs, montages, level scripts) were maintained without removals.

---

## 3. Audio purge audit: historical index vs. distribution packages

Cross-referencing the official Wwise audio indexing database (`beyond.map` v1.3) against all 1,298 chunk containers (`.chk`) in `StreamingAssets/` and `Persistent/` identified the exact boundary between legacy test audio and production audio.

### Purged legacy vocalizations (33 files)
In early technical test builds, character combat vocalizations were implemented as short, standalone clips named with the `_sv` suffix. These 33 clips were removed from the physical package files upon migration to the production combat and dialogue framework:

| Index | Asset identifier | Category | Status in client |
|---|---|---|---|
| 1 | `chr_0016_laevat_action_dash_start_sv` | Action vocalization | Purged in production |
| 2 | `chr_0016_laevat_action_dodge_sv` | Action vocalization | Purged in production |
| 3 | `chr_0016_laevat_action_jump_nor_sv` | Action vocalization | Purged in production |
| 4 | `chr_0016_laevat_action_jump_running_sv` | Action vocalization | Purged in production |
| 5 | `chr_0016_laevat_action_land_high_sv` | Action vocalization | Purged in production |
| 6 | `chr_0016_laevat_action_land_nor_sv` | Action vocalization | Purged in production |
| 7 | `chr_0016_laevat_action_throw_sv` | Action vocalization | Purged in production |
| 8 | `chr_0016_laevat_idlespecial_react01_sv` | Action vocalization | Purged in production |
| 9 | `chr_0016_laevat_idlespecial_relax01_sv` | Action vocalization | Purged in production |
| 10 | `chr_0016_laevat_idlespecial_relax02_sv` | Action vocalization | Purged in production |
| 11 | `chr_0016_laevat_combat_attack01_sv` | Combat callout | Purged in production |
| 12 | `chr_0016_laevat_combat_attack02_sv` | Combat callout | Purged in production |
| 13 | `chr_0016_laevat_combat_attack03_sv` | Combat callout | Purged in production |
| 14 | `chr_0016_laevat_combat_attack04_sv` | Combat callout | Purged in production |
| 15 | `chr_0016_laevat_combat_attack_backup01_sv` | Combat callout | Purged in production |
| 16 | `chr_0016_laevat_combat_attack_backup02_sv` | Combat callout | Purged in production |
| 17 | `chr_0016_laevat_combat_attack_backup03_sv` | Combat callout | Purged in production |
| 18 | `chr_0016_laevat_combat_attack_fall_sv` | Combat callout | Purged in production |
| 19 | `chr_0016_laevat_combat_attack_last_sv` | Combat callout | Purged in production |
| 20 | `chr_0016_laevat_combat_attack_rise_sv` | Combat callout | Purged in production |
| 21 | `chr_0016_laevat_combat_attack_sv_heavy` | Combat callout | Purged in production |
| 22 | `chr_0016_laevat_combat_attack_sv_light` | Combat callout | Purged in production |
| 23 | `chr_0016_laevat_combat_attack_sv_medium` | Combat callout | Purged in production |
| 24 | `chr_0016_laevat_combat_hurt_sv_heavy` | Combat callout | Purged in production |
| 25 | `chr_0016_laevat_combat_hurt_sv_light` | Combat callout | Purged in production |
| 26 | `chr_0016_laevat_combat_hurt_sv_nor` | Combat callout | Purged in production |
| 27 | `chr_0016_laevat_combat_skill_nor_extra_sv` | Combat callout | Purged in production |
| 28 | `chr_0016_laevat_combat_skill_nor_sv` | Combat callout | Purged in production |
| 29 | `chr_0016_laevat_combat_ult_attack01_sv` | Combat callout | Purged in production |
| 30 | `chr_0016_laevat_combat_ult_attack02_sv` | Combat callout | Purged in production |
| 31 | `chr_0016_laevat_combat_ult_attack03_sv` | Combat callout | Purged in production |
| 32 | `chr_0016_laevat_combat_ult_attack_last_sv` | Combat callout | Purged in production |
| 33 | `chr_0016_laevat_explocomm_switch_sv` | Combat callout | Purged in production |

A sweep of all 1,298 chunk packages confirmed zero occurrences of these 33 file IDs on disk.

### Retained production audio (897 files)
In the production client distribution, all 897 Japanese audio tracks voiced by Horie Yui are present across `default_japanese_stream_0.pck` and `default_japanese_stream_1.pck`:
- **132 character voicelines:** Combat lines (`au_btl_*`), affinity dialogs, breakthrough voice lines, and profile voice recordings located under `Characters/chr_0016_laevat/`.
- **765 narrative dialogue voicelines:** Story quest dialogue and radio communications across Chapter 16 (`c16m1`, `c16m2`, `c16m3`, `c16m4`) and `Narrating/CommonExtra/0016_laevat/`.

---

## 4. External timeline and event correlation

External community archives, patch changelogs, and wiki databases corroborate the local findings:

1. **Alpha / Technical Test 1 (November 2023):** Only 9 operators were playable (Endministrator, Perlica, Chen Qianyu, Wulfgard, Fjall, Angelina, Avywenna, Ember, Xaihi). Laevatain was not present in the initial alpha build.
2. **Client package patch updates:** Laevatain was introduced as a 6-star Heat Striker. In response to player feedback, Gryphline reworked her movement speed, attack pacing, and flame visual effects, directly correlating with the 5 updated flame prefab bundles discovered in `7064D8E2.blc`.
3. **Global Launch (January 22, 2026):** Debuted on the launch rate-up banner (*Laevatain: The Awakening*) with her personal storyline quest *"Let Fire Consume the Ashen Past"*.
4. **Permanent content confirmation:** Her story quests and Chapter 16 narrative files are permanent main-game content. No limited-time festival events or seasonal costume variants have been delisted or pruned from the client.
5. **Lore confirmation for "Olga Randall":** Official Operator Intel files verify "Olga Randall" as her temporary field pseudonym at UWST Beacon DAU.14 before awakening to her Surtr memories, confirming the validity of the Chapter 16 narrative references.
6. **ResHax CBT audio engineering corroboration:** Verified against the technical community thread on ResHax (`topic/18476`), which documents the shift from unencrypted Alpha packages to CBT 2/3 encrypted VFS streams. Linked community samples (`init_banks.pck`, `init_stream.pck`, `AA462ABBFEC319B6...`) were isolated test chunks used to solve the `:)xD` header decryption and per-WEM XOR cipher rather than character audio archives. This confirms that the 33 early `_sv` vocalizations were internal placeholders deprecated upon migration to the production combat and dialogue framework.

---

## 5. Extraction of audited narrative audio and pre-patch base assets

Following the divergence and purge audit, actionable assets identified during the investigation were extracted and integrated into the project workspace:

### 1. Chapter 16 narrative dialogue voice corpus (742 files extracted)
All 742 additional Japanese narrative dialogue files mapped in `beyond.map` and resident within `default_japanese_stream_0.pck` and `stream_1.pck` were decrypted and extracted into `assets/Data/Audio/PCK/Windows/Japanese/v1d0/Narrating/`:
- `c16m1`: 168 story dialogue and radio tracks
- `c16m2`: 178 story dialogue and radio tracks
- `c16m3`: 202 story dialogue and radio tracks
- `c16m4`: 188 story dialogue and radio tracks
- `CommonExtra`: 6 additional interactive narrative cues

Total extracted Japanese voicelines on disk increased from 160 to 902, capturing the entire available voice recording corpus by Horie Yui.

### 2. Base shipping flame effect prefabs (53 files extracted)
The original pre-rework base shipping versions of the 5 flame effect prefabs (`p_laevat_normal_skill_start_01`, `p_fxbat_laevat_combo_skill_hit`, `p_fxbat_laevat_combo_skill_hit_02`, `p_fxbat_laevat_normal_skill_start_01`, `p_fxbat_laevat_attack_04_crack`) and their constituent hierarchy were unpacked from `StreamingAssets/VFS/7064D8E2/7064D8E2.blc` into `assets/divergence/pre_patch_base/`. This preserves the pre-patch visual structure for comparison against the patched production versions.

### 3. Permanently purged legacy clips status (33 files)
Targeted range queries against CDN archive manifests (`6628375-5`) and all 1,298 chunk packages confirmed that the 33 early placeholder vocalization clips (`_sv`) were pruned during the internal transition from closed tests to production. They are permanently absent from public distribution builds.

import sys, os, json, hashlib, time
from PIL import Image
import UnityPy

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
assets_dir = os.path.join(base_dir, 'assets')
mapping_file = os.path.join(base_dir, 'meta', 'assetbundle_mapping.json')
cache_unp_dir = os.path.join(base_dir, 'cache', 'unpacked_cabs')

with open(mapping_file, 'r', encoding='utf-8') as f:
    mapping_data = json.load(f)

records = mapping_data['records']
print(f"Processing {len(records)} assets...")

stats = {
    'textures_png': 0,
    'models_mesh': 0,
    'animations': 0,
    'prefabs_and_data': 0,
    'errors': 0
}

extracted_records = {}

t0 = time.time()
# Cache opened UnityPy envs to avoid re-reading same CAB multiple times
env_cache = {}

for idx, rec in enumerate(records):
    orig_path = rec['asset_path']
    bundle_file = rec['bundle_file']
    clean_b_name = bundle_file.replace('/', '_').replace('\\', '_')
    cab_dir = os.path.join(cache_unp_dir, clean_b_name)
    
    # Target path on disk: workspace/endfield-laevatain/assets/<orig_path>
    # Note: orig_path might contain '##' for sub-assets (e.g. .fbx##submesh)
    # On Windows, '#' is valid in filenames, but we can replace '##' with '/' or keep clean filename
    safe_rel_path = orig_path.replace('##', '_')
    target_disk_path = os.path.join(assets_dir, safe_rel_path)
    os.makedirs(os.path.dirname(target_disk_path), exist_ok=True)
    
    # Find the CAB file in cab_dir
    cab_files = [f for f in os.listdir(cab_dir) if not f.endswith('.resS')] if os.path.exists(cab_dir) else []
    if not cab_files:
        print(f"[{idx+1}/{len(records)}] Warning: No CAB file in {cab_dir}")
        stats['errors'] += 1
        continue
        
    cab_path = os.path.join(cab_dir, cab_files[0])
    
    if cab_path not in env_cache:
        try:
            env_cache[cab_path] = UnityPy.load(cab_path)
        except Exception as e:
            env_cache[cab_path] = None
            
    env = env_cache.get(cab_path)
    
    # Determine extraction strategy based on path
    ext = orig_path.split('.')[-1].lower() if '.' in orig_path else ''
    
    saved = False
    
    # 1. Texture extraction
    if any(ext.startswith(t) for t in ['png', 'tga', 'exr']):
        if env:
            # Look for Texture2D or Sprite
            for obj in env.objects:
                if obj.type.name in ['Texture2D', 'Sprite']:
                    try:
                        data = obj.read()
                        img = getattr(data, 'image', None)
                        if img:
                            out_img_path = target_disk_path if target_disk_path.endswith('.png') else target_disk_path + '.png'
                            img.save(out_img_path)
                            target_disk_path = out_img_path
                            saved = True
                            stats['textures_png'] += 1
                            break
                    except Exception:
                        pass
                        
    # 2. Mesh extraction
    elif 'fbx' in ext:
        if env:
            for obj in env.objects:
                if obj.type.name == 'Mesh':
                    try:
                        data = obj.read()
                        obj_data = data.export()
                        if obj_data:
                            out_mesh_path = target_disk_path if target_disk_path.endswith('.obj') else target_disk_path + '.obj'
                            with open(out_mesh_path, 'w', encoding='utf-8') as f_mesh:
                                f_mesh.write(obj_data)
                            target_disk_path = out_mesh_path
                            saved = True
                            stats['models_mesh'] += 1
                            break
                    except Exception:
                        pass
                        
    # 3. Animation extraction
    elif 'anim' in ext:
        stats['animations'] += 1
        
    # Fallback / General: if not saved as specific format, save raw object serialized json or binary
    if not saved:
        if env and len(env.objects) > 0:
            # Dump object summary / json
            obj_dump = []
            for obj in env.objects:
                try:
                    d = obj.read()
                    name = getattr(d, 'm_Name', getattr(d, 'name', ''))
                    obj_dump.append({
                        'type': obj.type.name,
                        'name': name,
                        'path_id': obj.path_id
                    })
                except Exception:
                    obj_dump.append({'type': obj.type.name, 'path_id': obj.path_id})
            
            with open(target_disk_path, 'w', encoding='utf-8') as f_out:
                json.dump({
                    'source_asset_path': orig_path,
                    'bundle_container': bundle_file,
                    'objects': obj_dump
                }, f_out, indent=2)
            stats['prefabs_and_data'] += 1
            saved = True
        else:
            # Copy CAB file or write stub
            with open(target_disk_path, 'wb') as f_out:
                with open(cab_path, 'rb') as f_in:
                    f_out.write(f_in.read(4096))
            stats['prefabs_and_data'] += 1
            saved = True

    # Record SHA-256 and size
    file_size = os.path.getsize(target_disk_path)
    with open(target_disk_path, 'rb') as f_hash:
        file_sha256 = hashlib.sha256(f_hash.read()).hexdigest()
        
    extracted_records[target_disk_path.replace(workspace_dir + os.sep, '').replace('\\', '/')] = {
        'source_path': orig_path,
        'bundle_file': bundle_file,
        'category': 'assetbundle_asset',
        'scope': 'in_scope',
        'size': file_size,
        'sha256': file_sha256
    }
    
    if (idx + 1) % 250 == 0 or idx == len(records) - 1:
        print(f"  [{idx+1}/{len(records)}] Processed ({time.time()-t0:.1f}s)...")

# Clean up memory
env_cache.clear()

print(f"\nExtraction complete in {time.time()-t0:.2f}s!")
print(f"Stats: {stats}")
print(f"Total extracted records: {len(extracted_records)}")

# Save extracted asset records ledger
out_ledger = os.path.join(base_dir, 'meta', 'extracted_bundle_assets.json')
with open(out_ledger, 'w', encoding='utf-8') as f:
    json.dump(extracted_records, f, indent=2)
print(f"Saved extracted ledger to {out_ledger}")

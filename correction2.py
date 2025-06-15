from PIL import Image
import os

image_dir = "path_to_your_instant-ngp\\build\\instant-ngp\\data\\v2obj\\images"  # or your actual image directory
for fname in os.listdir(image_dir):
    fpath = os.path.join(image_dir, fname)
    try:
        with Image.open(fpath) as img:
            img.verify()
        print(f"✅ OK: {fname}")
    except Exception as e:
        print(f"❌ ERROR: {fname} - {e}")

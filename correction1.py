import json
import os

with open("transforms.json", "r") as f:
    data = json.load(f)

for frame in data["frames"]:
    # Keep only filename, replace path
    fname = os.path.basename(frame["file_path"])
    frame["file_path"] = f"images/{os.path.splitext(fname)[0]}"

with open("transforms.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ transforms.json updated.")

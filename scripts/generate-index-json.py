import os
import json
import shutil

# Paths (relative to scripts/generate-index-json.py)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
YML_SRC = os.path.join(SCRIPT_DIR, "..", "yml")
YML_DST = os.path.join(SCRIPT_DIR, "..", "exfiltration-ui", "public", "yml")

EXCLUDED = {"YML-Schema.yml", "YML-Template.yml", "Allowed-Tags-and-Categories.yml"}

# Ensure destination exists
os.makedirs(YML_DST, exist_ok=True)

# Gather and copy .yml files
yml_files = []
for fname in os.listdir(YML_SRC):
    if fname.endswith(".yml") and fname not in EXCLUDED:
        shutil.copy2(os.path.join(YML_SRC, fname), os.path.join(YML_DST, fname))
        yml_files.append(fname)

# Write index.json
with open(os.path.join(YML_DST, "index.json"), "w") as f:
    json.dump(sorted(yml_files), f, indent=2)

print(f"{len(yml_files)} .yml files copied and index.json generated.")

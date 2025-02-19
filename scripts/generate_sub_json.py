import json
import os

# Define the paths
MASTER_JSON_PATH = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/assets/master_data.json"
OUTPUT_DIR = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/assets/filtered_jsons"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load master.json dynamically
def load_master_json():
    if not os.path.exists(MASTER_JSON_PATH):
        print(f"❌ Error: {MASTER_JSON_PATH} not found.")
        return []

    with open(MASTER_JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        print(f"🔍 Loaded Master JSON: {json.dumps(data, indent=2)}")  # Debugging
        return data

# Get affected view types (Replace with dynamic values from your PR script)
affected_viewtypes = {"TYPE_0", "TYPE_1"}

# Load the master JSON
MASTER_JSON = load_master_json()

# Generate sub JSONs
for viewtype in affected_viewtypes:
    sub_json = [entry for entry in MASTER_JSON if entry["view"]["type"] == viewtype]

    if sub_json:
        file_path = os.path.join(OUTPUT_DIR, f"{viewtype}.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(sub_json, json_file, indent=4)

        print(f"✅ Sub JSON created: {file_path}")
    else:
        print(f"⚠️ No data found for {viewtype}")

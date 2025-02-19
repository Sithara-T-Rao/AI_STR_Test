import requests
import re
import sys
import os
import json
from colorama import Fore, Style, init

# GitHub API token and repo details
REPO_OWNER = "Sithara-T-Rao"
REPO_NAME = "AI_STR_Test"
PR_NUMBER = sys.argv[1] if len(sys.argv) > 1 else "1"  # PR number from command line argument

# Paths for master JSON and output directory
MASTER_JSON_PATH = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/assets/master_data.json"
OUTPUT_DIR = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/assets/filtered_jsons"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Headers for authentication
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}

def get_pr_diff():
    """Fetch diff of a PR."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/files"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Error fetching PR diff: {response.json()}")
        return []

    return response.json()  # Return the list of file changes in the PR

def extract_viewtypes(diff_files, viewholder_factory_file):
    """Extract affected ViewTypes from PR diff."""
    affected_viewtypes = set()
    viewholder_factory_types = extract_viewholder_factory_types(viewholder_factory_file)

    for file in diff_files:
        diff_text = file.get("patch", "")  # Get the diff patch content for the file
        for line in diff_text.split("\n"):
            if line.startswith("+"):  # Consider only added lines
                for type_name in viewholder_factory_types:
                    if type_name in line:
                        affected_viewtypes.add(type_name)  # Add the matched types

    return affected_viewtypes

def extract_viewholder_factory_types(viewholder_factory_file):
    """Dynamically extract constants (e.g., TYPE_0, TYPE_1) from the ViewHolderFactory file."""
    if not os.path.exists(viewholder_factory_file):
        print(f"❌ Error: The file {viewholder_factory_file} does not exist.")
        return []

    with open(viewholder_factory_file, "r") as file:
        content = file.read()
    return re.findall(r"\b(TYPE_\w+)\b", content)

def load_master_json():
    """Load the master JSON file."""
    if not os.path.exists(MASTER_JSON_PATH):
        print(f"❌ Error: {MASTER_JSON_PATH} not found.")
        return []

    with open(MASTER_JSON_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def generate_sub_jsons(affected_viewtypes, master_json):
    """Generate filtered JSON files based on affected view types."""
    for viewtype in affected_viewtypes:
        sub_json = [entry for entry in master_json if entry["view"]["type"] == viewtype]

        if sub_json:
            file_path = os.path.join(OUTPUT_DIR, f"{viewtype}.json")
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(sub_json, json_file, indent=4)

            print(f"✅ Sub JSON created: {file_path}")
        else:
            print(f"⚠️ No data found for {viewtype}")

def main():
    # Get the list of files changed in the PR
    diff_files = get_pr_diff()

    # Specify the location of the ViewHolderFactory file in your project
    viewholder_factory_file = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/java/com/example/ai_str_test/ViewHolderFactory.kt"

    # Extract affected ViewTypes
    affected_viewtypes = extract_viewtypes(diff_files, viewholder_factory_file)

    print(Fore.GREEN + f" ✅ Affected ViewTypes: {', '.join(affected_viewtypes) if affected_viewtypes else 'None'}")

    if not affected_viewtypes:
        print(Fore.YELLOW + "⚠️ No affected ViewTypes found, skipping JSON generation.")
        return

    # Load master JSON
    master_json = load_master_json()

    # Generate sub JSONs for affected view types
    generate_sub_jsons(affected_viewtypes, master_json)

if __name__ == "__main__":
    main()

import requests
import re
import sys
import os
from colorama import Fore, Style, init

# GitHub API token and repo details
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "Sithara-T-Rao"
REPO_NAME = "AI_STR_Test"
PR_NUMBER = sys.argv[1] if len(sys.argv) > 1 else "1"  # PR number from command line argument

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
        # print(f"Error fetching PR diff: {response.json()}")
        return []

    # print(f"Successfully fetched PR diff: {response.status_code}")
    return response.json()  # Return the list of file changes in the PR

def extract_viewholders_and_viewtypes(diff_files, viewholder_factory_file):
    """Extract affected ViewHolders and ViewTypes from PR diff."""
    affected_viewholders = set()
    affected_viewtypes = set()

    # Dynamically extract types from ViewHolderFactory class
    viewholder_factory_types = extract_viewholder_factory_types(viewholder_factory_file)

    for file in diff_files:
        diff_text = file.get("patch", "")  # Get the diff patch content for the file

        # print(f"Processing file: {file.get('filename')}")  # Debugging line
        for line in diff_text.split("\n"):
            # Consider only added lines
            if line.startswith("+"):
                # Extract ViewHolder class names (only class definitions)
                class_match = re.findall(r"class\s+(\w+ViewHolder)\b", line)
                if class_match:
                    affected_viewholders.update(class_match)  # Add the class names

                # Check if any of the ViewHolderFactory types are referenced
                for type_name in viewholder_factory_types:
                    if type_name in line:
                        affected_viewtypes.add(type_name)  # Add the matched types

    return affected_viewholders, affected_viewtypes


def extract_viewholder_factory_types(viewholder_factory_file):
    """Dynamically extract constants (e.g., TYPE_0, TYPE_1) from the ViewHolderFactory file."""
    if not os.path.exists(viewholder_factory_file):
        print(f"Error: The file {viewholder_factory_file} does not exist.")
        return []

    viewholder_factory_types = []
    with open(viewholder_factory_file, "r") as file:
        content = file.read()
        # print(f": The file {content}  exist.")
        # Match all constants of the form `val TYPE_* = ...` or `const val TYPE_* = ...`
        viewholder_factory_types = re.findall(r"\b(TYPE_\w+)\b", content)
        # print(f": The viewholder_factory_types are { viewholder_factory_types}  exist.")
    return viewholder_factory_types

def main():
    # Get the list of files changed in the PR
    diff_files = get_pr_diff()

    # Specify the location of the ViewHolderFactory file in your project
    viewholder_factory_file = "/Users/sithararao/AndroidStudioProjects/AI_STR_Test/app/src/main/java/com/example/ai_str_test/ViewHolderFactory.kt"

    # Extract affected ViewHolders and ViewTypes
    affected_viewholders, affected_viewtypes = extract_viewholders_and_viewtypes(diff_files, viewholder_factory_file)

    # Print out the affected ViewHolders and ViewTypes
    print(Fore.GREEN + " ✅ Affected ViewHolders :", ", ".join(affected_viewholders) if affected_viewholders else "None")
    print(Fore.GREEN + " ✅ Affected ViewTypes :", ", ".join(affected_viewtypes) if affected_viewtypes else "None")

if __name__ == "__main__":
    main()

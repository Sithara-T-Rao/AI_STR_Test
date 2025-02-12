import os
from github import Github

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))

# Get repository and pull request details
repo = g.get_repo("Sithara-T-Rao/AI_STR_Test")
pr_number = os.getenv('PR_NUMBER')
pr = repo.get_pull(int(pr_number))

# Get the changed files
changed_files = pr.get_files()

# Analyze changed files
changed_item_types = set()
affected_viewholders = set()

for file in changed_files:
    if file.filename.endswith(".kt") or file.filename.endswith(".java"):
        patch = file.patch
        if "RecyclerView" in patch:
            changed_item_types.add(file.filename)
            if "ViewHolder" in patch:
                affected_viewholders.add(file.filename)

# Save analysis results
with open(".github/scripts/analysis.txt", "w") as f:
    f.write(f"Changed Item Types: {list(changed_item_types)}\n")
    f.write(f"Affected ViewHolders: {list(affected_viewholders)}\n")

import os
from github import Github

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))

# Get repository and pull request details
repo = g.get_repo("Sithara-T-Rao/AI_STR_Test")
pr_number = os.getenv('PR_NUMBER')
pr = repo.get_pull(int(pr_number))

# Read analysis results
with open(".github/scripts/analysis.txt", "r") as f:
    analysis_result = f.read()

# Post comment on PR
pr.create_issue_comment(f"### Analysis Result\n\n{analysis_result}")

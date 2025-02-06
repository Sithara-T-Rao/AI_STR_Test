import os
import google.generativeai as genai

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Read PR diff
with open("pr_diff.txt", "r") as file:
    pr_diff = file.read()

# Define the AI prompt
prompt = f"""
Analyze the following GitHub PR diff and classify ViewHolders and ViewTypes into:
- Newly added (with file path and suggested placement)
- Updated (with what was changed)
- Edited (with recommendations on what to add/remove)

Provide the output in **YAML format**.

PR Diff:
{pr_diff}

Format:
```yaml
newly_added:
  - ViewHolderName: "..."
    File: "..."
    SuggestedPlacement: "Inside RecyclerView Adapter XYZ"
    SuggestedCode: |
      class NewViewHolder extends RecyclerView.ViewHolder {{
          public NewViewHolder(View itemView) {{
              super(itemView);
              // Initialize views properly here
          }}
      }}

updated:
  - ViewHolderName: "..."
    File: "..."
    Changes: "..."
    SuggestedEdits: |
      - Modify method XYZ to improve efficiency
      - Change ViewBinding approach

edited:
  - ViewHolderName: "..."
    File: "..."
    Changes: "..."
    Suggestions: |
      - Remove deprecated method XYZ
      - Add a new parameter for better flexibility

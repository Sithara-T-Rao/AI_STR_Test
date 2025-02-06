import os
import google.generativeai as genai

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Read PR diff
with open("pr_diff.txt", "r") as file:
    pr_diff = file.read()

# Define the AI prompt (properly closed triple quotes)
prompt = """Analyze the following GitHub PR diff and classify ViewHolders and ViewTypes into:
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
      class NewViewHolder extends RecyclerView.ViewHolder {
          public NewViewHolder(View itemView) {
              super(itemView);
              // Initialize views properly here
          }
      }

updated:
  - ViewHolderName: "..."
    File: "..."
    Changes: "Detailed description of what was changed"

edited:
  - ViewHolderName: "..."
    File: "..."
    Recommendations: "Suggestions on what to add/remove"
```"""

# Generate the analysis
response = model.generate_text(prompt)

# Save the output to a YAML file
with open("pr_analysis_output.yaml", "w") as output_file:
    output_file.write(response.text)

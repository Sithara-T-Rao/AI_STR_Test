import openai
import os

# Load API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Read PR diff
with open("diff.txt", "r", encoding="utf-8") as f:
    diff_content = f.read()

# Define the prompt
prompt = f"""
Analyze the following PR diff. Identify the changed RecyclerView item types and the affected ViewHolders.

{diff_content}

Summarize in the format:
- **Changed Item Types**: [List]
- **Affected ViewHolders**: [List]
- **Key Modifications**: [Brief summary]
"""

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert in Android development."},
        {"role": "user", "content": prompt}
    ]
)

# Get response text
analysis_result = response["choices"][0]["message"]["content"]

# Save analysis output
with open("analysis.txt", "w", encoding="utf-8") as f:
    f.write(analysis_result)

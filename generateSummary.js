const { execSync } = require('child_process');
const axios = require('axios');

async function summarizeChanges() {
  try {
    // Step 1: Get a summary of the changed files
    const diff = execSync('git diff --stat origin/main').toString();
    
    console.log("Extracted PR Changes:\n", diff);

    // Step 2: Send changes to Hugging Face AI for summarization
    const response = await axios.post(
      'https://api-inference.huggingface.co/models/facebook/bart-large-cnn',
      { inputs: `Summarize these code changes:\n\n${diff}` },
      {
        headers: {
          Authorization: `Bearer hf_YOUR_ACCESS_TOKEN`, // Replace with your Hugging Face token (optional)
        },
      }
    );

    const summary = response.data[0]?.summary_text || "Could not generate summary.";
    console.log("\nPR Summary:", summary);
    return summary;

  } catch (error) {
    console.error("Error generating PR summary:", error);
    return "Error summarizing PR changes.";
  }
}

summarizeChanges();

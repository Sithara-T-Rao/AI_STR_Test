const axios = require('axios');
const { execSync } = require('child_process');

// Fetch the latest commit message (or diff) as an example input
function getCommitMessages() {
    try {
        const commitMessage = execSync('git log -1 --pretty=%B').toString().trim();
        console.log("Commit Message:", commitMessage);  // Debugging line to log the commit message
        return commitMessage;
    } catch (error) {
        console.error("Error fetching commit message:", error);
        return "";
    }
}

// Function to call the Hugging Face API for summary
async function getSummaryFromAI(text) {
    try {
        const response = await axios.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",  // Example model
            { inputs: text },
            {
                headers: {
                    Authorization: `Bearer ${process.env.HUGGING_FACE_API_KEY}`,
                },
            }
        );
        console.log("Summary from AI:", response.data[0].summary_text);  // Debugging line to log AI output
        return response.data[0].summary_text;
    } catch (error) {
        console.error("Error calling Hugging Face API:", error);
        return "Failed to generate summary.";
    }
}

// Main function to generate summary
async function generateSummary() {
    const commitMessages = getCommitMessages();
    
    if (!commitMessages) {
        console.log("No commit message found.");
        return "No changes detected in this PR.";
    }

    // Send commit message or diff to Hugging Face API for summarization
    const summary = await getSummaryFromAI(commitMessages);
    
    console.log("Final Summary:", summary);  // Debugging line to ensure summary is not empty
    return summary;
}

// Generate summary and print it
generateSummary().then((summary) => {
    console.log("Generated Summary:", summary);  // Output summary to console (GitHub Action will capture this)
});

const axios = require('axios');

// Example commit message or PR text
const commitMessage = "This PR adds a new feature that improves RecyclerView performance.";

// Send request to Hugging Face's model (e.g., BART for summarization)
async function getSummaryFromAI(text) {
    try {
        const response = await axios.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",  // Using a BART model
            { inputs: text },
            {
                headers: {
                    Authorization: `Bearer ${process.env.HUGGING_FACE_API_KEY}`,
                },
            }
        );
        return response.data[0].summary_text;
    } catch (error) {
        console.error("Error fetching summary from Hugging Face:", error);
        return "Failed to generate summary.";
    }
}

// Call the summarization function
getSummaryFromAI(commitMessage).then((summary) => {
    console.log("Generated Summary:", summary); // Log the summary for debugging
});

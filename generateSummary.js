const axios = require('axios');

// Fetch the Hugging Face API key from environment variables
const API_KEY = process.env.HUGGING_FACE_API_KEY;

// Get the PR description (or commit message) passed as a command line argument
const prDescription = process.argv[2];

if (!prDescription) {
    console.error("No text provided for summarization.");
    process.exit(1);
}

async function getSummaryFromAI(text) {
    try {
        // API request to Hugging Face’s model for summarization (BART model)
        const response = await axios.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",  // Hugging Face's BART model for summarization
            { inputs: text },
            {
                headers: {
                    Authorization: `Bearer ${API_KEY}`,  // Include the API key in the header
                }
            }
        );

        // Return the summary text
        return response.data[0].summary_text;
    } catch (error) {
        console.error("Error fetching summary from Hugging Face:", error.response ? error.response.data : error);
        return "Failed to generate summary.";
    }
}

// Call the summarization function and log the result
getSummaryFromAI(prDescription).then((summary) => {
    console.log(summary);  // Output the summary
});

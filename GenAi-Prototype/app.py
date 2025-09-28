# import packages
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()


# Get Gemini API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
	raise ValueError("GEMINI_API_KEY not found in environment. Please set it in your .env file.")

# Configure Gemini client
genai.configure(api_key=api_key)

# Create a model instance (Gemini Pro)
#model = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel("models/gemini-1.0-pro")

# Send a prompt and get a response
response = model.generate_content("Explain generative AI in one sentence.")

# Print the response
print(response.text)
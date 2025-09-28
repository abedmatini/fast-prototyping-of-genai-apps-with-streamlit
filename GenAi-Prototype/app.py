# import packages
from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment. Please set it in your .env file.")


st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Configure Gemini client
genai.configure(api_key=api_key)

# Create a model instance (Gemini Pro)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Send a prompt and get a response
response = model.generate_content("Explain generative AI in one sentence.")

# Print the response from Gemini
# print(response.text)
st.write(response.text)

# run the app with: streamlit run app.py
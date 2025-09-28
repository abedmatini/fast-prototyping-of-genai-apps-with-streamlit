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

# Configure Gemini client
genai.configure(api_key=api_key)

@st.cache_data
def get_gemini_response(user_prompt, temperature):
    # Configure safety settings to be less restrictive
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH", 
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        }
    ]
    
    # Create a model instance (Gemini Pro) with relaxed safety settings
    model = genai.GenerativeModel(
        "models/gemini-2.5-flash",
        safety_settings=safety_settings
    )
    
    try:
        # Send a prompt and get a response (simple approach like debug version)
        response = model.generate_content(user_prompt)
        
        # Simple approach - just return the text like in debug version
        return response.text
        
    except Exception as e:
        return f"❌ Error generating response: {str(e)}"

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app with Gemini API.")

# Add a text input box for the user prompt
user_prompt = st.text_input("Enter your prompt:", "Explain generative AI in one sentence.")

# Add a slider for temperature
temperature = st.slider(
    "Model temperature:",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.01,
    help="Controls randomness: 0 = deterministic, 2 = very creative"
    )

# Get response with caching
with st.spinner("AI is working..."):
    response_text = get_gemini_response(user_prompt, 0.7)  # Use fixed temperature for now
    
    # Display the response from Gemini
    st.write(response_text)

# run the app with: streamlit run app.py
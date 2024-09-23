import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get response from the newer OpenAI API
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use 'gpt-4' if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # Setting up the assistant role
            {"role": "user", "content": prompt}  # User's input
        ],
        max_tokens=150,  # Adjust token limit as needed
        temperature=0.7,  # Adjust for creativity
    )
    return response['choices'][0]['message']['content']

# Streamlit layout
st.title("Exelsior Chatbot")

# Input from the user
user_input = st.text_input("You:", "Hello, how can I assist you today?")

# If input is provided, get the response from OpenAI
if user_input:
    response = get_response(user_input)
    st.text_area("Seven of Nine:", value=response, height=200, max_chars=None)

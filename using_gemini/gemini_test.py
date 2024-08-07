"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyClnOnxcwExwbdGAwgaD0MaTSRBaM7hXOY")

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
    history=[]
)

# Send a message to the chat session
response = chat_session.send_message("How is your day?")

response_text = ''.join([part.text for part in response.parts])

# Print the extracted text
print(response_text)

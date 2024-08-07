import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyClnOnxcwExwbdGAwgaD0MaTSRBaM7hXOY")

# List available models
try:
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"Model ID: {model['name']}, Display Name: {model['displayName']}")
except Exception as e:
    print(f"An error occurred while listing models: {e}")

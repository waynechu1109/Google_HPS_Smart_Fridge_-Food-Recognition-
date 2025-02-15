from google.cloud import vision
from google.oauth2 import service_account
import google.generativeai as genai
import io

# Initialize the model correctly
model_name = "gemini-1.5-pro-latest"  # Desired model name
# model_name = "gemini-1.5-flash-8b-exp-0827" 

# Define the path to the image
image_path = "test_images/000010.JPG"

# Define the number of the kind of food we want to detect in the image
num_kind = 1

# =================================================================================================================

# Set up Google Cloud Vision API credentials
credentials = service_account.Credentials.from_service_account_file('gen-lang-client-0841175445-a7b8df25933b.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

# Set up Generative AI API key
genai.configure(api_key="AIzaSyBjfGIaKXnXZaQqp72UghpcDjnBFu7tRC0")

# Set up generation config
generation_config = {
    "temperature": 0.7,  # Lower temperature for more focused output
    "top_p": 0.95,
    "top_k": 50,  # Slightly lower top_k for more concentrated predictions
    "max_output_tokens": 512,  # Reduced max tokens for efficiency
    "response_mime_type": "text/plain",
}

# Read image and convert to binary
def load_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    return content

# Analyze image content for text and object labels
def analyze_image(image_path):
    image = vision.Image(content=load_image(image_path))
    
    # Extract text from image
    text_response = client.text_detection(image=image)
    texts = text_response.text_annotations
    
    # Extract full text
    full_text = ""
    if texts:
        full_text = texts[0].description.strip()
    
    # Handle Vision API errors
    if text_response.error.message:
        raise Exception(f'Vision API Text Error: {text_response.error.message}')

    # Detect labels (objects) in the image
    label_response = client.label_detection(image=image)
    labels = label_response.label_annotations

    # Extract label descriptions
    label_descriptions = []
    for label in labels:
        label_descriptions.append(label.description)
    
    # Handle Vision API errors
    if label_response.error.message:
        raise Exception(f'Vision API Label Error: {label_response.error.message}')
    
    return full_text, label_descriptions

# Extract text and objects from the image using the image path
extracted_text, object_descriptions = analyze_image(image_path)

# Generate the prompt for the Gemini model
prompt_text = (
    f"Below are the details extracted from an image that has already been analyzed:\n"
    f"Text in the image: {extracted_text}\n"
    f"The following foods were identified in the image: {', '.join(object_descriptions)}.\n"
    f"Please be very specific in identifying **exact food names** (such as 'scrambled egg' instead of generic terms like 'food').\n"
    f"Based on the image, provide the name of the food with **precise identification**, "
    f"and format the response as a JSON object (make sure the indentation is correct). "
    f"For each food, list the top {num_kind} kinds of food with the highest confidence percentages, along with their respective expiry dates or estimated storage days.\n"
    f"Make sure the food names are **clear and commonly recognized**, avoiding generic terms like '食物' or 'food.'\n"
    f"Moreover, include the **exact total quantity** of each kind of food, without breaking it down into different types or varieties.\n"
    f"For example, if the image contains 3 oranges, regardless of their specific types, the response should be:\n"
    f"object: [{{'text': 'orange', 'quantity': '3', 'confidence': '90%'}}]\n"
    f"For foods without packaging, provide estimated storage days based on your knowledge, treating the food as fresh. "
    f"If no expiry date is available, estimate the storage days based on general knowledge.\n"
    f"Each response should be **detailed and concise**, focusing solely on the requested information.\n"
    f"Output format:\n"
    f"1. 'object': Array of {{'text': '<name of the food>', 'quantity': '<quantity>', 'confidence': '<confidence percentage>'}}\n"
    f"2. 'expiry': Array of {{'text': '<expiry date (MUST be in the format of **MM/DD/YYYY**) or number of storage days>', 'type': 'days' or 'date', 'confidence': '<confidence percentage>'}}\n"
    f"3. 'location': Array of {{'object': {{'text': '<location description>', 'confidence': '<confidence percentage>'}}}}\n"
    f"The length of all the arrays **must be exactly {num_kind}** to match the number of top foods identified.\n"
    f"Ensure that the JSON response is structured accordingly, without any additional information beyond what is requested.\n"
    f"Additionally, please **DO NOT include** ```json and ``` at the beginning and the end of your response. Thank you.\n"
    f"Responses must be provided in Traditional Chinese and ensure there is an empty line between each section in the response.\n"
    f"Before finalizing the response, ensure that you have only included the total count for each food type, without specifying different varieties."
)


# Generate text using the Generative AI API
try:
    # Initialize the model
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config
    )
    
    # Start a chat session
    chat_session = model.start_chat(history=[])
    
    # Send the message
    response = chat_session.send_message(prompt_text)
    
    # Extract and print the generated text
    response_text = ''.join([part.text for part in response.parts])
    print("\nGenerated Response:")
    print(response_text)
    
except Exception as e:
    print(f"An error occurred: {e}")

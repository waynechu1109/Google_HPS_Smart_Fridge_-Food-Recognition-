from google.cloud import vision
from google.oauth2 import service_account
import google.generativeai as genai
import io
import json

# Initialize the model correctly
model_name = "gemini-1.5-pro-latest"  # Desired model name

inputJSON = '''[
  {
    "expiresIn": 5,
    "object": "Apple"
  },
  {
    "expiresIn": 14,
    "object": "Banana"
  },
  {
    "expiresIn": 1,
    "object": "Carrot"
  },
  {
    "expiresIn": 1,
    "object": "Bread"
  },
  {
    "expiresIn": 1,
    "object": "Cheese"
  },
  {
    "expiresIn": 10,
    "object": "Milk"
  },
  {
    "expiresIn": 12,
    "object": "Eggs"
  },
  {
    "expiresIn": 13,
    "object": "Tomato"
  },
  {
    "expiresIn": 2,
    "object": "Chicken"
  },
  {
    "expiresIn": 5,
    "object": "Orange"
  },
  {
    "expiresIn": 5,
    "object": "Yogurt"
  },
  {
    "expiresIn": 23,
    "object": "Potato"
  }
]'''

# inputJSON = """[{"expiresIn":180,"object":"卡迪那 寶卡卡 海鹽口味"},{"expiresIn":7,"object":"飲料"},{"expiresIn":7,"object":"檸檬"},{"expiresIn":1,"object":"น้ำจิ้มไก่ (แม่ประนอม)"}]"""

# 將 JSON 物件轉換為字串
json_data = json.loads(inputJSON)
formatted_json = json.dumps(json_data, indent=2)  # 格式化 JSON 以嵌入到 prompt

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
    "max_output_tokens": 8000,  # Reduced max tokens for efficiency
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

# Generate the prompt for the Gemini model
prompt_text = (
    f"You received a json array which contains some food and their respective expiration day as follow.\n"
    f"{formatted_json}\n\n"
    f"Based on these information, please provide me with a recipe that utilizes these foods.\n"
    f"Please **IGNORE** the ingredients such as 'foods,' '食物,' 'drinks,' or '飲料' that is unclear about what specific ingredient is used.\n"
    f"Remember to use the ingredients with fewer expiration days first\n"
    f"Finally, please translate **ALL** your response into **Traditional Chinese** and **do not** show the English part, thank you!\n"
    f"Make sure you only print the output **ONCE**, do not duplicate the same output.\n"
)

# prompt_text = (
#     f"You have received a JSON array that contains a list of foods and their respective expiration dates, as follows:\n"
#     f"{formatted_json}\n\n"
#     f"Based on this information, please create a recipe using these ingredients.\n"
#     f"Please **IGNORE** the ingredients with general name such as 'foods,' '食物,' 'drinks,' or '飲料,' and focus only on **specific ingredients**.\n"
#     f"Prioritize using ingredients with the shortest expiration dates first.\n"
#     f"Finally, please translate **all** of your response into **Traditional Chinese** without showing any part in English. Thank you!\n"
# )

# f"and list the ingredients with their remaining expiration days.\n"

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

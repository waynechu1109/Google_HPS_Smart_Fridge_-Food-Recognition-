from google.cloud import vision
from google.oauth2 import service_account
import google.generativeai as genai
import io

# Initialize the model correctly
model_name = "gemini-1.5-pro-latest"  # 欲使用的模型名稱

# Define the path to the image
image_path = "test_images/000020.JPG"

# =================================================================================================================

# 設定 Google Cloud Vision API 的憑證
credentials = service_account.Credentials.from_service_account_file('gen-lang-client-0841175445-3c8fcf49ac4d.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

# 設定 Generative AI 的 API 金鑰
genai.configure(api_key="AIzaSyClnOnxcwExwbdGAwgaD0MaTSRBaM7hXOY")

# 設定生成配置
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# 讀取圖片並轉換為二進制格式
def load_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    return content

# 分析圖片的內容，提取文字和物品描述
def analyze_image(image_path):
    image = vision.Image(content=load_image(image_path))
    
    # 提取文字
    text_response = client.text_detection(image=image)
    texts = text_response.text_annotations
    
    # 提取所有的文字
    full_text = ""
    if texts:
        full_text = texts[0].description.strip()
    
    # 處理Vision API的錯誤
    if text_response.error.message:
        raise Exception(f'Vision API Text Error: {text_response.error.message}')

    # 標籤檢測來描述物品
    label_response = client.label_detection(image=image)
    labels = label_response.label_annotations #

    # 提取所有標籤描述
    label_descriptions = []
    for label in labels:
        label_descriptions.append(label.description)
    
    # 處理Vision API的錯誤
    if label_response.error.message:
        raise Exception(f'Vision API Label Error: {label_response.error.message}')
    
    return full_text, label_descriptions

# 使用圖片路徑來提取圖片中的文字和物品描述
extracted_text, object_descriptions = analyze_image(image_path)

# 創建一個問題或提示文本
prompt_text = (
    f"The image contains the following text: {extracted_text}\n"
    f"The image seems to have the following objects: {', '.join(object_descriptions)}.\n"
    f"Based on the objects and text identified in the image, please pick the most possible object. List the object with its probabilities.\n"

    f"- Be specific in your identification: for example, specify the type of fruit or food rather than using a general term like \"food.\"\n"
    f"- If multiple objects are identified, list all of them with their respective probabilities.\n"
    f"- If you can find the expiry date of any object, please include it in the format MM/DD/YYYY and explain where did you find the expiry date of the item. If there is no apparent expiry date shown, show \"None\"\n"

    f"Format your response exactly as follows: \n"
    f"Objects: [The only one object that is most likely to be] Probability: [confidence percentages] Expiry Date: [MM/DD/YYYY], [the place you found it]\n"

    f"Please do not include any additional text or explanation beyond this specified format."
)

# Generate text using the Generative AI API
try:
    # 初始化模型
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config
    )
    
    # 開始聊天會話
    chat_session = model.start_chat(history=[])
    
    # 發送消息
    response = chat_session.send_message(prompt_text)
    
    # 提取和印出生成的文本
    response_text = ''.join([part.text for part in response.parts])
    print("\nGenerated Response:")
    print(response_text)
    
except Exception as e:
    print(f"An error occurred: {e}")

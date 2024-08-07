import pyimgur
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
from PIL import Image
import os

# 設定API密鑰
IMGUR_CLIENT_ID = "12867c708be2612"
OPENAI_API_KEY = "Your_OpenAI_API_Key"

# 讀取圖片
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'test_images', '3.jpeg')
image = Image.open(image_path)
image.show()

# 上傳圖片到Imgur
im = pyimgur.Imgur(IMGUR_CLIENT_ID)
uploaded_image = im.upload_image(image_path, title="Uploaded with PyImgur")
print("The image is successfully uploaded. URL: ", uploaded_image.link)

# 使用OpenAI API問問題
question = f"請問這張圖片 {uploaded_image.link} 有什麼特別之處？"

response = client.chat.completions.create(model="gpt-4",
messages=[
    {"role": "user", "content": question}
])

answer = response.choices[0].message.content
print("ChatGPT's answer: ", answer)

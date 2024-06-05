import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


class Image_Response:

    def __init__(self,input_prompt,image):
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        self.output = self.get_genai_image_response(input_prompt,image)

    def get_genai_image_response(self,input_prompt,image):
        img = PIL.Image.open(image)
        response = self.model.generate_content([input_prompt, img]) 
        return response.text
    
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


class AllModel:

    def __init__(self):
       self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def summarize(self,input_doc):
        prompt = """you are an intelligent assistant using the giving document summarize it correctly and shortly
        document:
        {document}
        """
        response = self.model.generate_content([prompt.format(document=input_doc)]) 
        return response.text

    def extract_keywords(self,inp_doc):
        prompt = """you are an intelligent assistant using the giving document extract the keywords in it correctly one by one
        document:
        {document}
        """
        response = self.model.generate_content([prompt.format(document=inp_doc)]) 
        return response.text
    
    def translate(self,inp_doc,lan):
        prompt = """you are an intelligent assistant using the giving document translate the doc in eng to {lang} and give it in correct format
        document:
        {document}
        """
        response = self.model.generate_content([prompt.format(document=inp_doc,lang=lan)]) 
        return response.text
    
    def sentiment_analysis(self,inp_doc):
        prompt = """you are an intelligent assistant using the giving document analyse the sentiment in short manner
        document:
        {document}
        """
        response = self.model.generate_content([prompt.format(document=inp_doc)]) 
        return response.text

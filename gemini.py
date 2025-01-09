import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GEMINI_KEY")

class GeminiLLM: 

    def __init__(self):
        genai.configure(api_key = GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text      
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError('GEMINI_API_KEY not found in .env file')
    return genai.Client(api_key=api_key)

def ask_gemini(prompt: str, system_context: str = '') -> str:
    client = get_client()
    full_prompt = f'{system_context}\n\n{prompt}' if system_context else prompt
    response = client.models.generate_content(
        model='gemini-1.5-flash-latest',
        contents=full_prompt
    )
    return response.text

if __name__ == '__main__':
    response = ask_gemini('Say hello in one sentence')
    print(response)
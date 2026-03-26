from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,  # Gemini uses 'contents'
        config={"temperature": 0.2},
    )
    return response.text  # Gemini uses .text directly, not .content[0].text

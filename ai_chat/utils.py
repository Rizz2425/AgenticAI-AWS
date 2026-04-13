import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("Warning: GROQ_API_KEY is not set! Check your .env or Environment Variables.")
    client = None
else:
    client = Groq(api_key=api_key)

def get_medical_advice(user_symptoms):
    if client is None:
        return "System Error: API Key is not configured correctly."

    system_prompt = {
        "role": "system",
        "content": (
            "You are a professional Medical AI Assistant. "
            "Analyze the symptoms provided by the user and suggest possible causes or diseases. "
            "Always include a disclaimer that you are an AI and the user should consult a real doctor."
        )
    }
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                system_prompt,
                {"role": "user", "content": f"I am feeling these symptoms: {user_symptoms}"}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI service: {str(e)}"
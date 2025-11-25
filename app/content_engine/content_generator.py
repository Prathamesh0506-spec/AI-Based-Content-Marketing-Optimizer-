import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

#Always load .env from Project root (2 levels up)
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

#Create Groq client using API key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_content(prompt: str) -> str:
    """
    Generate a single piece of AI content using Groq's Llama model.
    Returns plain text string.
    """
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating content: {e}"


# ---------------- DEMO ----------------
if __name__ == "__main__":
    topic = "AI in Digital Marketing"
    prompt = f"Write a short LinkedIn post about {topic} highlighting its benefits."
    
    print("\n🔹 Prompt Sent:")
    print(prompt)
    
    content = generate_content(prompt)
    print("\nGenerated Content:\n")
    print(content)

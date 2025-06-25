# llm/prompt_to_code.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def prompt_to_code(user_prompt: str, column_list: list) -> str:
    system_prompt = f"""
You are a helpful AI assistant. The DataFrame is named df, and NumPy is available as np.

Generate valid, executable Python code using pandas and/or NumPy to clean the data based on the instruction.

Do NOT include explanations, markdown, or comments. Only return code.

DataFrame columns: {column_list}
    """

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # or "llama3-8b-8192"
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.4,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("[ERROR] Groq SDK failed:", e)
        return "# Error: Groq SDK failed"

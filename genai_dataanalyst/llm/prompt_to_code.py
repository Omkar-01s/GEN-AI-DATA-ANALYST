# llm/prompt_to_code.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def prompt_to_code(user_prompt: str, column_list: list) -> str:
    system_prompt = f"""

You are a helpful professional level Python Data Analyst AI assistant. The DataFrame is named df, and NumPy is available as np.

Generate valid, write compact and production quality executable Python code using pandas and/or NumPy to clean the data based on the instruction.

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
    

def transform_prompt_to_code(user_prompt: str, column_list: list) -> str:
    system_prompt = f"""
You are a helpful professional-level Python Data Analyst AI assistant.

You perform advanced data transformations using `pandas`, `numpy`, `re` (regex), and `sklearn.preprocessing`.

The DataFrame is always named `df`. NumPy is available as `np`.

Your job is to convert natural language instructions into clean, compact, production-quality Python code.

### Rules:
Return only valid, executable Python code
No explanations, markdown, or comments
Use only: pandas, numpy, re, sklearn.preprocessing
Optimize the code — avoid unnecessary steps

### Example Transformations You Can Handle:
Label encoding, one-hot encoding, binning, scaling
Regex-based text cleaning
Z-score or MinMax normalization
Extracting features from strings or datetime
Creating new columns based on logic

DataFrame columns: {column_list}

Instruction: {user_prompt}
"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.4,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("[ERROR] Groq SDK (transform) failed:", e)
        return "# Error: Groq SDK failed to generate transformation code"


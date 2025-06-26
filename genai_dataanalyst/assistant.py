# assistant.py

import pandas as pd
from genai_dataanalyst.llm.prompt_to_code import prompt_to_code, transform_prompt_to_code 
from genai_dataanalyst.executor.safe_exec import safe_exec

class AnalystAssistant:
    """
    AnalystAssistant is a GenAI-powered data analyst helper that takes a DataFrame and a natural language
    cleaning or transformation prompt, uses a LLaMA model to generate Python code, safely executes it,
    and returns the updated DataFrame.
    """

    def __init__(self, model="llama3-8b-8192"):
        self.model_name = model  # LLM name (for future switching or logging)

    def clean(self, df: pd.DataFrame, prompt: str) -> pd.DataFrame:
        """
        Clean the DataFrame based on a natural language instruction using pandas/NumPy only.
        """
        print(f"[INFO] [CLEAN] Prompt: {prompt}")
        generated_code = prompt_to_code(prompt, df.columns.tolist())
        print("[DEBUG] [CLEAN] Generated Code:\n", generated_code)
        return safe_exec(df.copy(), generated_code)

    def transform(self, df: pd.DataFrame, prompt: str) -> pd.DataFrame:
        """
        Transform the DataFrame based on advanced instructions using pandas, NumPy, regex, sklearn, etc.
        """
        print(f"[INFO] [TRANSFORM] Prompt: {prompt}")
        generated_code = transform_prompt_to_code(prompt, df.columns.tolist())
        print("[DEBUG] [TRANSFORM] Generated Code:\n", generated_code)
        return safe_exec(df.copy(), generated_code)

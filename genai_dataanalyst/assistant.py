# assistant.py

import pandas as pd
from genai_dataanalyst.llm.prompt_to_code import prompt_to_code
from genai_dataanalyst.executor.safe_exec import safe_exec

class AnalystAssistant:
    """
    AnalystAssistant is a lightweight GenAI helper that takes a DataFrame and a natural language cleaning prompt,
    uses a LLaMA 70B model to convert that into Python (pandas) code, safely executes it,
    and returns the updated DataFrame.
    """

    def __init__(self, model="llama3-8b-8192"):
        self.model_name = model  # Can be used to switch models later if needed

    def clean(self, df: pd.DataFrame, prompt: str) -> pd.DataFrame:
        """
        Clean the DataFrame based on a natural language instruction.

        Parameters:
        - df (pd.DataFrame): The input dataset to clean
        - prompt (str): Natural language cleaning instruction

        Returns:
        - pd.DataFrame: The updated dataset after applying the transformation
        """

        print(f"[INFO] Received prompt: {prompt}")

        # Step 1: Generate cleaning code using LLaMA 3 (70B) model
        generated_code = prompt_to_code(prompt, df.columns.tolist())

        print("[DEBUG] Generated Code:\n", generated_code)

        # Step 2: Execute the code on the input DataFrame safely
        cleaned_df = safe_exec(df.copy(), generated_code)

        return cleaned_df

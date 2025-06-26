# executor/safe_exec.py

import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler

def safe_exec(df: pd.DataFrame, code: str) -> pd.DataFrame:
    """
    Safely execute the LLM-generated pandas / NumPy / sklearn transformation code on the DataFrame.
    """
    local_vars = {
        "df": df.copy(),
        "np": np,
        "pd": pd,
        "re": re,
        "LabelEncoder": LabelEncoder,
        "MinMaxScaler": MinMaxScaler,
        "StandardScaler": StandardScaler
    }

    try:
        exec(code, {}, local_vars)  # Restrict global scope
        result_df = local_vars["df"]
        return result_df

    except Exception as e:
        print("[ERROR] Code execution failed:", e)
        print("[DEBUG] Failed code was:\n", code)
        return df.copy()

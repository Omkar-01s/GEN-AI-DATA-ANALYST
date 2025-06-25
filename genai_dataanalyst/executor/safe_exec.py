# executor/safe_exec.py

import pandas as pd
import numpy as np  # ✅ Added NumPy

def safe_exec(df: pd.DataFrame, code: str) -> pd.DataFrame:
    """
    Safely execute the LLM-generated pandas or NumPy code on the input DataFrame.
    """
    local_vars = {
        "df": df.copy(),
        "np": np  # ✅ Allow NumPy access in local scope
    }

    try:
        exec(code, {}, local_vars)  # Restrict global scope
        result_df = local_vars["df"]
        return result_df

    except Exception as e:
        print("[ERROR] Code execution failed:", e)
        print("[DEBUG] Failed code was:\n", code)
        return df.copy()
# If execution fails, return a copy of the original DataFrame
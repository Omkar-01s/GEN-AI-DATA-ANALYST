import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
 
from genai_dataanalyst.llm.prompt_to_code import prompt_to_code, transform_prompt_to_code, visualize_prompt_to_code
from genai_dataanalyst.executor.safe_exec import safe_exec

class AnalystAssistant:
    """
    AnalystAssistant is a GenAI-powered data analyst helper that takes a DataFrame and a natural language
    cleaning or transformation prompt, uses a LLaMA model to generate Python code, safely executes it,
    and returns the updated DataFrame.
    """

    def __init__(self, model="llama3-8b-8192"):
        self.model_name = model  # LLM name (for future switching or logging)
        self._charts = []        # Store charts for reuse in KPI layout

    def clean(self, df: pd.DataFrame, prompt: str) -> pd.DataFrame:
        """
        Clean the DataFrame based on a natural language instruction using pandas,NumPy, datetime etc.
        """
        print(f"[INFO] [CLEAN] Prompt: {prompt}")
        generated_code = prompt_to_code(prompt, df.columns.tolist())
        print("[DEBUG] [CLEAN] Generated Code:\n",generated_code)
        return safe_exec(df.copy(), generated_code)

    def transform(self, df: pd.DataFrame, prompt: str) -> pd.DataFrame:
        """
        Transform the DataFrame based on advanced instructions using pandas, NumPy, regex, sklearn, etc.
        """
        print(f"[INFO] [TRANSFORM] Prompt: {prompt}")
        generated_code = transform_prompt_to_code(prompt, df.columns.tolist())
        print("[DEBUG] [TRANSFORM] Generated Code:\n", generated_code)
        return safe_exec(df.copy(), generated_code)
    
    def visualize(self, df: pd.DataFrame, prompt: str, name: str = None):
        """
        Generate a Plotly visualization based on a natural language prompt, and store it for reuse in kpi().
        """
        print(f"[INFO] [VISUALIZE] Prompt: {prompt}")
        code = visualize_prompt_to_code(prompt, df.columns.tolist())
        print("[DEBUG] [VISUALIZE] Code:\n", code)

        local_vars = {"df": df.copy(), "go": go}
        try:
            exec(code, {}, local_vars)
            fig = local_vars.get("fig")

            if fig:
                self._charts.append({
                    "fig": fig,
                    "name": name or prompt,
                    "prompt": prompt
                })
                fig.show()
            else:
                print("[ERROR] No figure generated.")

        except Exception as e:
            print("[ERROR] Failed to render chart:", e)
            print("[DEBUG] Code was:\n", code)

    def kpi(self, layout_prompt: str = ""):
        """
        Use stored charts and assemble a dashboard layout using a natural language layout_prompt.
        """
        print(f"[INFO] [KPI] Assembling dashboard layout...")

        if not self._charts:
            print("[WARN] No charts to display.")
            return

        try:
            # For now, default to 2x2 grid layout (can later use LLM to parse layout_prompt)
            rows = 2
            cols = 2
            fig = make_subplots(rows=rows, cols=cols, subplot_titles=[c["name"] for c in self._charts])

            for i, chart in enumerate(self._charts):
                row = (i // cols) + 1
                col = (i % cols) + 1
                for trace in chart["fig"].data:
                    fig.add_trace(trace, row=row, col=col)

            fig.update_layout(height=800, width=1000, title_text="📊 KPI Dashboard")
            fig.show()

        except Exception as e:
            print("[ERROR] Failed to assemble KPI dashboard:", e)

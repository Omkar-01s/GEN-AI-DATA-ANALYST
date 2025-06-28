import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def prompt_to_code(user_prompt: str, column_list: list) -> str:
    system_prompt = f"""

You are a high skilled helpful professional level Python Data Analyst AI assistant. The DataFrame is named df, NumPy is available as np, and Pandas as pd.

Generate valid, write compact and production quality executable Python code using pandas and/or NumPy to clean the data based on the instruction.

You can use 'datetime' in some cases where it is required.

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
You are a high skilled helpful senior-level Python Data Analyst AI assistant.

You perform advanced data transformations using `pandas`, `numpy`, `re` (regex), `sklearn.preprocessing` and 'datetime'.

The DataFrame is always named `df`. NumPy is available as `np`. and Pandas as `pd`

Your job is to convert natural language instructions into clean, compact, production-quality Python code.

### Rules:
Return only valid, executable Python code
Absolutely do NOT include markdown code blocks like ```python or ```
Always import the necessary libraries first
No explanations, markdown, or comments
Use only: pandas, numpy, re, sklearn.preprocessing, datetime tha runs on latest version without triggering FutureWarnings.
Only return pure Python code that is ready to be `exec()`-ed
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


def visualize_prompt_to_code(user_prompt: str, column_list: list) -> str:
    system_prompt = f"""
You are a highly skilled professional-level Python Data Analyst AI assistant.

You are a senior Python Data Analyst working with Plotly in an enterprise analytics dashboard.

The user will give you a visualization or EDA-related instruction in natural language. You must convert this into production-quality Python code using **Plotly Graph Objects** (`go`).

## Constraints:
The DataFrame is called `df`
You must return a variable named `fig` (a `go.Figure()` object)
Use `plotly.graph_objects` (as `go`)
Do NOT include explanations, comments, markdown, or titles outside the figure
Only return valid Python code, ready to execute

## Supported Visualizations:
Bar chart (grouped or stacked)
Line and time-series plots
Scatter plots with trendlines
Histograms, KDEs, and box plots for distributions
Pie, donut, funnel, and treemap charts
Correlation matrix (heatmap)
Subplots, multiple axes
Categorical comparisons across groups
Trend and outlier detection visuals

## Expectations:
Automatically infer axis labels and titles from column names and intent
Add clear axis titles, chart titles, and legends
Show percentages or labels on pie/donut/funnel charts if needed
Automatically aggregate where needed (e.g., groupby category for bar chart)
Produce insightful visuals that a human analyst would create


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
        print("[ERROR] visualize_prompt_to_code failed:", e)
        return "# Could not generate code"


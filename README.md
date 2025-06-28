# 📊 InsightsGen: Automating Data Analyst Workflow with Generative AI

InsightsGen is a **GenAI powered Data Analyst Assistant** that transforms how analysts interact with data. By converting **natural language instructions** into **executable Python (pandas, NumPy) code**, this system automates core data tasks like cleaning, transformation, visualization, and KPI dashboard creation.

---

## 🚀 Key Features

### 🧹 1. Natural Language Data Cleaning
- Converts human instructions into pandas/NumPy code using **LLaMA 3 via Groq API**
- Handles missing values, formatting issues, categorical replacements, and more
- ⚡ **70% reduction** in manual coding time

### 🔄 2. High-Accuracy Data Transformations
- Performs complex operations like feature engineering, regex cleaning, scaling, and encoding
- Uses advanced libraries like **scikit-learn**, **regex**, and datetime
- Optimized prompt template ensures **reliable and production-quality code**

### 📊 3. Smart Visualizations with Plotly
- Interprets natural language EDA prompts and generates **interactive charts**
- Supports bar, pie, line, boxplots, correlation heatmaps, subplots, and more
- Charts are **saved and reused** for KPI assembly

### 📈 4. KPI Dashboard Assembly
- Automatically **builds dashboards** from previously generated charts
- Uses natural language to decide layout positions and structure
- Built on **Plotly Subplots**, great for embedding or reporting

### 🔐 5. Safe Execution Sandbox
- All generated code is run in a **secure `safe_exec()` environment**
- Supports:
  - pandas, NumPy
  - sklearn preprocessing
  - regex, datetime
  - Plotly (go)

---

## 🧠 Tech Stack

| Component     | Stack                          |
|---------------|---------------------------------|
| LLM Backend   | LLaMA 3 (via Groq API)         |
| Frameworks    | Python, groq, langchain
| Visualization | Plotly                         |
| Execution     | `exec()` sandbox with restricted scope |
| IDE           | VS Code, Jupyter Notebook      |

---

## 📂 Project Structure
GEN-AI-DATA-ANALYST/
├ ── genai_dataanalyst/
│ ├ ── assistant.py # Main Assistant class
│ ├ ── llm/
│ │ ├ ── prompt_to_code.py # LLM prompt-to-code logic (clean, transform, visualize)
│ ├ ── executor/
│ │ ├ ── safe_exec.py # Executes code securely
├ ── examples/
│ ├ ── demo.ipynb # Usage examples and tests
├ ── requirements.txt # Project dependencies
├ ── .env # Groq API key


---

## 🧪 Example Usage

```python
from genai_dataanalyst.assistant import AnalystAssistant
import pandas as pd

df = pd.read_csv("sales.csv")
assistant = AnalystAssistant()

# Clean
df = assistant.clean(df, prompt="Replace 'M' with 'Men' and 'W' with 'Women' in Gender column.")

# Transform
df = assistant.transform(df, prompt="Create 'Age_Group' column based on 'Age' ranges.If below 18 child, between 18 to 50 as Adult and Above 50 to 100 as senior")

# Visualize
assistant.visualize(df, prompt="Show bar chart of total sales per region.", name="Sales by Region")

# Build Dashboard
assistant.kpi(layout_prompt="Place the sales bar chart in top-left.")
```

💡 Real-World Impact
|Problem Solved | How InsightsGen Helps           |
|---------------|---------------------------------|
| Manual coding for cleaning & EDA | Auto-generates pandas code from plain logic natural language |
| Slower turnaround on data tasks	 | Reduces task time by up to 70% |
| No centralized charting for KPIs | Reuses charts and assembles them dynamically |
| High chance of syntax / import errors| Uses safe_exec() and fine-tuned prompts |



	

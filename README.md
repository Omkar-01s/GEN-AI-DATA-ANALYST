# 📊 InsightsGen: Automating Data Analyst Workflow with Generative AI

InsightsGen is a production-ready **GenAI-powered Data Analyst Assistant** that transforms how analysts interact with data. By converting **natural language instructions** into **executable Python (pandas, NumPy) code**, this system automates core data tasks like cleaning, transformation, visualization, and KPI dashboard creation.

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
| Frameworks    | Python, Streamlit              |
| Visualization | Plotly                         |
| Execution     | `exec()` sandbox with restricted scope |
| IDE           | VS Code, Jupyter Notebook      |

---

## 📂 Project Structure


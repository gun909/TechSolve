# TechSolve
Data Preparation, Power BI Dashboard and Local AI Agent. NOTE: This project only uses Mock data for training purposes.

## Project Overview

This project was completed as part of the Data & AI Specialist Practical Assessment.

The project analyses synthetic customer support ticket data for TechSolve IT, a fictional managed service provider. The goal is to improve visibility into customer support performance, identify operational trends and problem areas, and demonstrate how AI can be used to interact with business data.

The project consists of three main parts:

1. Data preparation and external data integration
2. Power BI data visualisation and analysis
3. AI Agent for natural-language data analysis

---

## Assessment Overview

| Assessment Section | Work Completed | Tool | Status | Evidence |
|---|---|---|---|---|
| **Part 1 – Data Preparation** | Cleaned ticket data, removed duplicates/nulls, integrated NZ public holiday data | Python / Pandas | ✅ Complete | GitHub files |
| **Part 2 – Visualisation** | Ticket overview, resolution time, CSAT, holiday impact and priority analysis | Power BI | ✅ Complete | `.pbix` / Screenshots |
| **Part 3 – AI Agent** | Natural-language dataset Q&A | LM Studio + Qwen3 + Streamlit | ✅ Complete | Python code + Demo video |
| **Review** | Methodology, tools, challenges, time spent and AI usage | Word / PDF | ✅ Complete | Review document |

---

## Part 1 – Source, Combine & Prepare

### Data Sources

The project uses:

- TechSolve synthetic customer support ticket data
- New Zealand public holiday data from Employment New Zealand

The public holiday dataset was selected to investigate whether holidays have an impact on ticket resolution times.

### Data Preparation

Python and Pandas were used to:

- Identify and remove duplicate records
- Handle missing values
- Select relevant columns for analysis
- Prepare cleaned datasets for Power BI
- Integrate external New Zealand public holiday information

---

## Part 2 – Power BI Visualisation

Power BI was used to analyse customer support performance.

The analysis includes:

- Ticket issue overview
- Monthly ticket trends
- Average resolution time
- Customer Satisfaction (CSAT)
- Holiday impact on resolution time
- CSAT vs resolution time
- Issue complexity analysis
- Subscription type and contract value analysis
- Ticket priority analysis

### Key Findings

The average resolution time was approximately **121 hours**.

There were some increases in resolution time around the late December and early January holiday period. However, the overall holiday impact did not appear significant compared with the average resolution time.

The lowest average customer satisfaction score identified in the analysis occurred in **September 2024**, with an average CSAT score of approximately **2.95**.

---

## Part 3 – AI Agent

A local AI-powered data analysis interface was developed to allow users to ask natural-language questions about the dataset.

### Technology

- **AI Platform:** LM Studio
- **Model:** Qwen3 4B
- **User Interface:** Streamlit
- **Data Analysis:** Python / Pandas

Example questions:

- Give me a data type and shape overview.
- Which months have the highest total tickets?
- What is the average CSAT score?

### Run the Application

Install the required Python packages:

    pip install -r requirements.txt

Run the Streamlit application:

    python -m streamlit run agent/app.py

LM Studio and the required local model must also be running for AI-powered responses.

---

## Project Structure

    TechSolve/
    │
    ├── agent/                          # AI Agent and Streamlit application
    ├── data_raw/                       # Original datasets
    ├── data_clean/                     # Cleaning code: Python
    ├── data_processed/                 # Processed analysis datasets
    ├── powerbi/                        # Power BI dashboard
    ├── Practical Assessment.docx       # Assessment review/documentation
    ├── requirements.txt                # Python dependencies
    └── README.md

> Note: The local Python virtual environment (`.venv`) is excluded from the repository.

---

## Tools Used

**Data Cleaning:** Python / Pandas

**Data Visualisation:** Microsoft Power BI

**AI Agent:** LM Studio + Qwen3

**AI Agent UI:** Streamlit

**Development & Version Control:** Git / GitHub

---

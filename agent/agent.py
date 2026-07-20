import pandas as pd
from openai import OpenAI

# -------------------------------------------------
# 1. Load dataset once
# -------------------------------------------------

CSV_PATH = "D:/AI_Workspace/Data/TechSolve_clean.csv"

df = pd.read_csv(CSV_PATH)

# Convert date field if it exists
if "ticket_created_date" in df.columns:
    df["ticket_created_date"] = pd.to_datetime(
        df["ticket_created_date"],
        errors="coerce"
    )

# -------------------------------------------------
# 2. Connect to local Qwen
# -------------------------------------------------

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="local-only"
)

MODEL_NAME = "qwen3-4b-2507"


# -------------------------------------------------
# 3. Create dataset summary
# -------------------------------------------------

def get_dataset_summary():
    return f"""
Dataset shape:
{df.shape}

Columns:
{df.columns.tolist()}

Data types:
{df.dtypes.to_string()}
"""


# -------------------------------------------------
# 4. Run safe predefined analysis
# -------------------------------------------------

def analyse_data(question: str):
    """
    Perform real Pandas calculations based on common
    business questions.

    Returns text containing calculated results.
    """

    q = question.lower()
# Average CSAT score
    if (
        "average" in q
        and (
            "csat_score" in q
            or "csat" in q
            or "customer satisfaction" in q
        )
    ):
        if "csat_score" not in df.columns:
            return "The csat_score column is not available."

        average_csat = df["csat_score"].mean()

        return f"""
Average CSAT score:

{average_csat:.2f}
"""

    # Total rows
    elif (
        "how many rows" in q
        or "total rows" in q
        or "number of rows" in q
        or "row count" in q
    ):
        return f"""
Total number of rows:

{len(df)}
"""
    # ---------------------------------------------
    # Customer satisfaction by month
    # ---------------------------------------------

    if (
        "customer satisfaction" in q
        or "csat" in q
        or "satisfaction" in q
    ) and "month" in q:

        if (
            "ticket_created_date" not in df.columns
            or "csat_score" not in df.columns
        ):
            return "Required columns are not available."

        temp = df.dropna(
            subset=["ticket_created_date", "csat_score"]
        ).copy()

        temp["month"] = (
            temp["ticket_created_date"]
            .dt.to_period("M")
            .astype(str)
        )

        result = (
            temp.groupby("month")["csat_score"]
            .mean()
            .sort_values()
        )

        return f"""
Average customer satisfaction by month:

{result.to_string()}

Lowest month:
{result.index[0]}

Lowest average satisfaction:
{result.iloc[0]:.2f}
"""

    # ---------------------------------------------
    # Ticket volume by month
    # ---------------------------------------------

    elif (
        "ticket" in q
        and "month" in q
        and (
            "volume" in q
            or "most" in q
            or "highest" in q
            or "number" in q
        )
    ):

        if "ticket_created_date" not in df.columns:
            return "ticket_created_date column is unavailable."

        temp = df.dropna(
            subset=["ticket_created_date"]
        ).copy()

        temp["month"] = (
            temp["ticket_created_date"]
            .dt.to_period("M")
            .astype(str)
        )

        result = (
            temp.groupby("month")
            .size()
            .sort_values(ascending=False)
        )

        return f"""
Ticket volume by month:

{result.to_string()}

Highest ticket volume month:
{result.index[0]}

Number of tickets:
{result.iloc[0]}
"""

    # ---------------------------------------------
    # Resolution time
    # ---------------------------------------------

    elif "resolution" in q and "time" in q:

        if "resolution_time_hours" not in df.columns:
            return "resolution_time_hours column is unavailable."

        average = df["resolution_time_hours"].mean()
        median = df["resolution_time_hours"].median()

        return f"""
Average resolution time:
{average:.2f} hours

Median resolution time:
{median:.2f} hours
"""

    # ---------------------------------------------
    # Issue complexity
    # ---------------------------------------------

    elif "complexity" in q:

        if "issue_complexity_score" not in df.columns:
            return "issue_complexity_score column is unavailable."

        result = (
            df["issue_complexity_score"]
            .value_counts(dropna=False)
            .sort_index()
        )

        return f"""
Issue complexity distribution:

{result.to_string()}
"""

    # ---------------------------------------------
    # Unknown question
    # ---------------------------------------------

    else:
        return """
No predefined Pandas analysis matched this question.

The AI should explain what analysis would be needed,
but must not invent numerical results.
"""


# -------------------------------------------------
# 5. Ask Qwen to explain calculated results
# -------------------------------------------------

def answer_question(question: str):

    calculated_result = analyse_data(question)

    dataset_summary = get_dataset_summary()

    prompt = f"""
You are a business data analysis assistant.

Dataset information:

{dataset_summary}

The user asked:

{question}

Python/Pandas calculated the following result:

{calculated_result}

Instructions:

1. Answer the user's question clearly.
2. Use ONLY the calculated results supplied above.
3. Never invent numbers.
4. If the calculation does not answer the question,
   explain what additional analysis is required.
5. Keep the answer concise and business-friendly.
"""

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful business data analyst. "
                    "Never invent numerical results."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    return response.choices[0].message.content

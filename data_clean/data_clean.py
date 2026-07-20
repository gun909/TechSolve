import pandas as pd

# ---------- 1. Load ----------------------------------------------------------
# uploaded file
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / ".." / "data_raw" / "TechSolve_raw_data.xlsx"
OUTPUT_CSV = BASE_DIR / ".." / "data_processed" / "TechSolve_clean.csv"

df = pd.read_excel(RAW_PATH)

# ---------- 2. Drop mandatory-field nulls ------------------------------------
key_cols = ["customer_name", "customer_email", "customer_id"]
df = df.dropna(subset=key_cols)

# ---------- 3. De-duplicate within each ticket_id ---------------------------
# “Similar” = identical **after** lower-casing & trimming whitespace
# (switch to fuzzy matching if you need looser rules later)

df["customer_name_std"] = df["customer_name"].str.lower().str.strip()
df["customer_email_std"] = df["customer_email"].str.lower().str.strip()

dupe_mask = (
    df.duplicated(subset=["ticket_id", "customer_name_std"], keep="first")
    | df.duplicated(subset=["ticket_id", "customer_email_std"], keep="first")
)
df = df[~dupe_mask].copy()           # keep the first occurrence, drop the rest

# ---------- 4. Select relevant columns ---------------------------------------
cols_to_keep = [
    "ticket_id",                 # key info
    "customer_id",
    "customer_email",
    "customer_segment",
    "account_manager",
    "monthly_contract_value",
    "subscription_type",
    "priority",
    "issue_description",          # what issues are raised
    "resolution_notes",           # how they’re handled
    "ticket_created_date",        # where improvement is possible
    "ticket_resolved_date",
    "first_response_time_hours",
    "resolution_time_hours",
    "csat_score",
    "issue_complexity_score",
]
df_clean = df[cols_to_keep]

# ---------- 5. Persist -------------------------------------------------------
df_clean.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Cleaned file written to {OUTPUT_CSV}  (rows: {len(df_clean):,})")

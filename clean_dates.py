import pandas as pd

df = pd.read_csv("retail_sales_messy_dates.csv", dtype={"Order_Date": "string"})
formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d %b %Y", "%Y/%m/%d"]

def parse(value):
    if pd.isna(value) or not str(value).strip():
        return pd.NaT, "Missing date", "Left blank; verify from source"
    for fmt in formats:
        try:
            return pd.to_datetime(str(value).strip(), format=fmt, errors="raise"), "", f"Parsed with {fmt}"
        except (ValueError, TypeError):
            pass
    return pd.NaT, "Invalid or unrecognized date", "Not guessed; verify from source"

results = [parse(v) for v in df["Order_Date"]]
df["Clean_Date"] = [d.strftime("%Y-%m-%d") if not pd.isna(d) else "" for d, _, _ in results]
df["Issue"] = [issue for _, issue, _ in results]
df.to_csv("cleaned_retail_sales.csv", index=False)

log = []
for (_, row), (date, issue, action) in zip(df.iterrows(), results):
    original = row["Order_Date"]
    if issue:
        log.append([row["Order_ID"], original, issue, action])
    elif str(original).strip() != date.strftime("%Y-%m-%d"):
        log.append([row["Order_ID"], original, "Inconsistent date format", action + "; standardized to YYYY-MM-DD"])
pd.DataFrame(log, columns=["Order_ID","Original_Date","Issue","Action_Taken"]).to_csv("date_issue_log.csv", index=False)

print("Total records:", len(df))
print("Valid dates:", sum(not pd.isna(d) for d, _, _ in results))
print("Missing/invalid dates:", sum(bool(i) for _, i, _ in results))

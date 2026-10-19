import pandas as pd
from pathlib import Path

def transform_sales(data):
    data["product"] = data["product"].str.title()
    data["revenue"] = data["quantity"] * data["unit_price"]
    return data


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "raw" / "sales.csv"
    data = pd.read_csv(csv_path)
    cleaned_data = transform_sales(data)
    print(cleaned_data)
    print("Total revenue:",cleaned_data["revenue"].sum())


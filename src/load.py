import sqlite3
import pandas as pd
from pathlib import Path
from extract import extract_sales
from transform import transform_sales


def load_sales(data,db_path):
    connection = sqlite3.connect(db_path)
    data.to_sql("sales",connection,if_exists="replace",index=False)
    connection.close()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    db_path = project_root / "data" / "sales.db"
    csv_path = project_root / "data" / "raw" / "sales.csv"
    sales_data = extract_sales(csv_path)
    cleaned_data = transform_sales(sales_data)
    load_sales(cleaned_data, db_path)
    print("Sales data loaded into SQLite successfully!")





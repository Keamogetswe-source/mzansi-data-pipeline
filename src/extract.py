import pandas as pd
from pathlib import Path

def extract_sales(file_path):
    """Read raw sales data from a CSV file."""

    if file_path.exists():
        data = pd.read_csv(file_path)
        print("Sales data extracted Successfully!")
        print(data.head())

        return data  
    else:
        raise FileNotFoundError("Sales file not found")
    


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "raw" / "sales.csv"
    
    sales_data = extract_sales(csv_path)
    print(f"\nTotal records: {len(sales_data)}")
        
   
   
  
    
    
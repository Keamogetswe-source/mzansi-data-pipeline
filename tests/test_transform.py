from src.transform import transform_sales
import pandas as pd

def test_transform_sales():
    data = pd.DataFrame({
        "product":["bread"],
        "quantity":[2],
        "unit_price":[15.0]
    })


    result = transform_sales(data)
    assert result["product"][0] == "Bread"
    assert result["revenue"][0] == 30.0

    
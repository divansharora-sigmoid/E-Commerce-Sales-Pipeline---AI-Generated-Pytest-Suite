import pandas as pd


def clean_sales_data(df):
    """
    Clean e-commerce sales data by handling null values.
    
    - Drops rows with null customer_id
    - Fills null sales_amount with 0
    
    Args:
        df: pandas DataFrame with sales data
        
    Returns:
        Cleaned pandas DataFrame
    """
    df = df.dropna(subset=["customer_id"])
    df["sales_amount"] = df["sales_amount"].fillna(0)
    return df

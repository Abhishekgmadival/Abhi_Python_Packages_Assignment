import pandas as pd

def total_and_average_sales(df, sales_column):
    """Print and return total and average sales for the given sales_column."""
    if sales_column not in df.columns:
        raise KeyError(f"Column '{sales_column}' not found in DataFrame")
    total = df[sales_column].sum()
    avg = df[sales_column].mean()
    # Return as tuple (total, avg)
    return total, avg

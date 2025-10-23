import pandas as pd

def remove_empty_rows(df):
    """Return a DataFrame with empty rows removed.
    A row is considered empty if all elements are NA or empty strings.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    # Replace empty strings with NaN, then drop rows where all elements are NaN
    cleaned = df.replace(r'^\s*$', pd.NA, regex=True).dropna(how='all')
    return cleaned.reset_index(drop=True)

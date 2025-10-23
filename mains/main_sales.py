import pandas as pd
from sales_tools import cleaning, report

def demo():
    # sample sales data with an empty row and some NaNs
    data = {
        'Region': ['North', 'South', '', 'East'],
        'Sales': [2500.0, 1800.5, None, 2200.0]
    }
    df = pd.DataFrame(data)
    print('Original DataFrame:')
    print(df)

    cleaned = cleaning.remove_empty_rows(df)
    print('\nCleaned DataFrame:')
    print(cleaned)

    total, avg = report.total_and_average_sales(cleaned, 'Sales')
    print(f"\nTotal Sales: {total}")
    print(f"Average Sales: {avg}")
if __name__ == '__main__':
    demo()

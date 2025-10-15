import pandas as pd
from pathlib import Path

def describe_df(df):
    """Describes a dataframe by printing its: shape, 1st and last 5 rows, column labels, column data types, info and pd describe
    
           Parameters:
           df (pandas.DataFrame): The dataframe to describe
    
           Returns:
           None
    
        """
    pd.set_option("display.max_columns", None)
    print(df.shape)
    print("\nFirst 5 rows:\n", df.head)
    print("\nLast 5 rows:\n", df.tail)
    print("\nColumns:\n", df.columns)
    print("\nData Types\n:", df.dtypes)
    print("\nInfo:\n", df.info)
    print("\nDescribe:\n", df.describe)

def check_data_quality(df):
    """Checks number of missing values and creates a copy of the data frame with only the rows with missing data
    
           Parameters:
           df (pandas.DataFrame): The dataframe to check
    
           Returns:
           None
    
        """
    total_missing_values = df.isnull().sum().sum()
    print(total_missing_values)
if __name__ == '__main__':
    data_file_raw =  Path(__file__).parent.parent.joinpath('data','paralympics_raw.csv')
    data_file_allraw = Path(__file__).parent.parent.joinpath('data','paralympics_all_raw.xlsx')
    raw_df = pd.read_csv(data_file_raw)
    all_raw_df1 =pd.read_excel(data_file_allraw)
    all_raw_df2 = pd.read_excel(data_file_allraw, sheet_name=1)
    check_data_quality(raw_df)
import pandas as pd
from pathlib import Path

# Locates data folder relative to current file
data = Path(__file__).parent.parent.parent.joinpath('Data')


#Collects all the .csv file paths in the data folder 
file_paths = sorted(data.glob("*.csv"), key = lambda f: int(f.stem[-4:]))

#Combines all the data files into one dataframe
flat_prices_df = pd.concat(
    [pd.read_csv(file_path).assign(source=file_path.stem) for file_path in file_paths],
    ignore_index = True
)
pd.set_option("display.max_columns", None)

#Outputs df to Tests folder without index numbers
tests = Path(__file__).parent.parent.parent.joinpath('Tests')
flat_prices_df.to_csv("Tests/Flat_Prices_Df.csv", index = False)

def overview():
    """Describes the basic structure and size of the df as well as the columns and their data types, also shows the first 5 rows as an example
    
           Parameters:
           df (pandas.DataFrame): The dataframe to describe
    
           Returns:
           None
    
        """
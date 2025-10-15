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
sdrgfsrgt

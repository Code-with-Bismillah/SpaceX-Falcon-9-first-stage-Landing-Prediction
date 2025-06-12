import pandas as pd

data = pd.read_csv('jupyter-labs-spacex-data-collection-api-v2.ipynb', engine='python', error_bad_lines=False)
print(data.head())

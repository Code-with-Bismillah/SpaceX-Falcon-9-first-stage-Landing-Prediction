import pandas as pd
import numpy as np

# Reconstruct the final dataframe from the notebook logic
# These are the columns used in the final data_falcon9 dataframe

columns = ['FlightNumber', 'Date', 'BoosterVersion', 'PayloadMass', 'Orbit', 'LaunchSite', 'Outcome', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial', 'Longitude', 'Latitude']

# Since we do not have the CSV, let's try to extract the data from the notebook if possible
# If not, this script will fail gracefully
try:
    import nbformat
    nb = nbformat.read('jupyter-labs-spacex-data-collection-api-v2.ipynb', as_version=4)
    code_cells = [cell['source'] for cell in nb.cells if cell['cell_type'] == 'code']
    # Look for a cell that prints or shows data_falcon9.head(), data_falcon9, or value_counts on relevant columns
    for cell in code_cells:
        if (
            ('data_falcon9' in cell and ('.head()' in cell or 'data_falcon9' in cell or 'print(data_falcon9' in cell)) or
            ('.value_counts()' in cell and (
                "LaunchSite" in cell or "Orbit" in cell or "Outcome" in cell))
        ):
            print('\n--- Relevant code cell ---')
            print(cell)
except Exception as e:
    print('Could not extract data from notebook:', e)



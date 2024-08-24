import pandas as pd

# Load the CSV file
df = pd.read_csv(r'files\2008beijing.csv')

# Replace â€¡ with an empty string in all columns
df.replace('â€¡', '', regex=True, inplace=True)

# Save the modified CSV back to a file
df.to_csv(r'files\2008beijing.csv', index=False)

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/2004_Summer_Olympics_medal_table'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

#table
table = soup.find_all('table', class_='wikitable sortable plainrowheaders jquery-tablesorter')[0]

title = table.find_all('th')

table_title = [title.text.strip() for title in title]

#create pandas dataframe
df = pd.DataFrame(columns=table_title)

# Drop all columns that are not in the specified list
columns_to_keep = ['Nation', 'Gold', 'Silver', 'Bronze', 'Total']
df = df.drop([col for col in df.columns if col not in columns_to_keep], axis=1)

column_data = table.find_all('tr')
for row in column_data[1:-1]:  # Skip the header row
    noc_data = row.find_all('th')
    medal_data = row.find_all('td')

    # Extract and clean data
    noc = [data.text.strip() for data in noc_data]
    medals = [data.text.strip() for data in medal_data]

    # Remove the first item from medals if its length is 5
    if len(medals) == 5:
        medals.pop(0)

    # Combine them into a single list
    combined_data = noc + medals

    length = len(df)
    df.loc[length] = combined_data

df.insert(0, 'Rank', range(1, len(df) + 1))
df = df[['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']]
df = df.rename(columns={'Nation':'NOC'})

print(df)
df.to_csv(r'files\2004athens.csv', index = False)

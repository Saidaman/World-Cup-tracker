import requests as req
from bs4 import BeautifulSoup as bs
import csv

wiki = req.get("https://en.wikipedia.org/wiki/FIFA_World_Cup")

soup = bs(wiki.content, 'html.parser')

tables = soup.find_all('table')

required_table = []
for table in tables:
    if table['class'] == ['wikitable', 'sortable']:
        required_table.append(table)

history_table = required_table[2]
header_tags = history_table.find_all('th')
headers = [header.text.strip() for header in header_tags]
headers = headers[0:12]
print(headers)

data_rows = history_table.find_all('tr')
rows = []
for row in data_rows:
    value = row.find_all('td')
    beautified_value = [ele.text.strip() for ele in value]

    if len(beautified_value) != 0:
        rows.append(beautified_value)

with open('world_cup_history.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
from bs4 import BeautifulSoup
import requests

# URL of the Wikipedia page containing the list of states and territories of the United States
url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'

# Send an HTTP GET request to fetch the content of the webpage
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the specific table on the page with the class "wikitable sortable mw-datatable sticky-header-multi sort-under plainrowheaders"
table_content = soup.find(class_="wikitable sortable mw-datatable sticky-header-multi sort-under plainrowheaders")

# Extract all rows from the table
rows = table_content.find_all('tr')

# Initialize an empty list to store the extracted data
data = []
for row in rows[2:]:  # Skip the first two rows (header and subheader)
    cells = row.find_all('td')  # Extract all cells from the row
    if len(cells) >= 4:  # Ensure the row has enough cells to include state and population data
        state = cells[0].text.strip()  # Extract and clean the state abbreviation from the first cell
        population = None
        for cell in cells:  # Iterate through all cells in the row
            div = cell.find('div')  # Look for a <div> element inside the cell
            if div and div.text.strip().replace(',', '').isdigit():  # Check if the content is a valid number
                population = int(div.text.strip().replace(',', ''))  # Convert the population string to an integer
                break  # Stop after finding the population
        data.append([state, population])  # Append the state and population as a list to the data list

import csv
# Open a new CSV file for writing the extracted data
with open('state_population.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)  # Create a CSV writer object
    # Write the header row with column names
    csvwriter.writerow(['State', 'Population'])
    # Write all the extracted state and population data to the CSV file
    csvwriter.writerows(data)

# Print the extracted state and population data
print("State and Population:")
for state, population in data:  # Iterate through the extracted data
    print(f"{state}: {population}")  # Print the state and its population

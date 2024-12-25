from bs4 import BeautifulSoup
import requests

# URL of the IMDb list to scrape
url = "https://www.imdb.com/list/ls056614673/"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Sending an HTTP GET request to fetch the page content
response = requests.get(url, headers=headers)

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all titles using their specific class
title = soup.find_all(class_="ipc-title__text")

# Extracting all stars (actors) using their specific class
star = soup.find_all(class_="ipc-link ipc-link--base dli-cast-item")

# Initialize an empty list to store star names
stars_list = []
for i in star:
    stars_list.append(i.text)  # Append the text (actor names) to the list

# Initialize an empty list to store movie titles
title_list = []
for i in title:
    title_list.append(i.get_text())  # Append the text (movie titles) to the list

# Initialize start and end indices for slicing the stars list
a = 0
b = 3

# Create an empty dictionary to store movie titles and their corresponding stars
dic = {}
for i in title_list:
    dic[i] = stars_list[a:b]  # Assign a slice of the stars list to each movie
    a += 3  # Move to the next set of 3 stars
    b += 3  # Update the end index for slicing

import csv

# Specify the output CSV file name
csv_file = "C:/Users/vivek/extracted_movies.csv"

# Write dictionary to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row for the CSV file
    writer.writerow(["Title", "Stars"])
    # Write each movie and its stars to the CSV file
    for title, stars in dic.items():
        writer.writerow([title, ", ".join(stars)])  # Combine the list of stars into a single string

# Print success message after writing to the CSV
print(f"Dictionary successfully written to {csv_file}")

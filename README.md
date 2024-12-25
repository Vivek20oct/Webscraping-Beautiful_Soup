# Web Scrapers: IMDb Movie Scraper and State Population Scraper

This repository contains two Python scripts for web scraping:  
1. **IMDb Movie Scraper**: Scrapes movie titles and their corresponding star cast from a specific IMDb list.  
2. **State Population Scraper**: Scrapes state names and populations from a Wikipedia page.  

Both scripts utilize **BeautifulSoup** for web scraping and **requests** for HTTP requests, exporting the data to CSV files for further analysis.

---

## IMDb Movie Scraper

### Features
- Scrapes movie titles and their cast from IMDb.
- Organizes the data into a dictionary format.
- Saves the scraped data into a CSV file.

### Requirements
- Python 3.x
- Required Libraries:
  - `BeautifulSoup4`
  - `requests`
  - `csv` (built-in)

Install required libraries:
```bash
pip install beautifulsoup4 requests
```

### How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/Vivek20oct/web-scrapers.git
   ```
2. Navigate to the project directory:
   ```bash
   cd web-scrapers
   ```
3. Run the IMDb scraper:
   ```bash
   python imdb_scraper.py
   ```
   - Fetches movies and casts from IMDb.
   - Saves the data to `extracted_movies.csv`.

### Output
The generated CSV (`extracted_movies.csv`) contains:
| Title               | Stars                             |
|---------------------|-----------------------------------|
| Dangal              | Aamir Khan, Sakshi Tanwar, ...   |
| Anand               | Rajesh Khanna, Amitabh Bachchan, ... |
| ...                 | ...                               |

---

## State Population Scraper

### Features
- Extracts data from the Wikipedia table of U.S. states and territories.
- Cleans and processes the data to extract state names and population numbers.
- Saves the extracted data into a CSV file and prints it for verification.

### Requirements
- Python 3.x
- Required Libraries:
  - `BeautifulSoup4`
  - `requests`
  - `csv` (built-in)

Install required libraries:
```bash
pip install beautifulsoup4 requests
```

### How to Use
1. Run the State Population scraper:
   ```bash
   python state_population_scraper.py
   ```
   - Fetches data from Wikipedia.
   - Saves the data to `state_population.csv`.
   - Prints the state and population data in the console.

### Output
The generated CSV (`state_population.csv`) contains:
| State      | Population |
|------------|------------|
| Alabama    | 5024279    |
| Alaska     | 733391     |
| ...        | ...        |

---

## File Structure
```
web-scrapers/
│
├── imdb_scraper.py          # Python script for IMDb scraping
├── state_population_scraper.py # Python script for Wikipedia scraping
├── extracted_movies.csv     # Output from IMDb scraper
├── state_population.csv     # Output from State Population scraper
└── README.md                # Project documentation
```

---

## Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it under the terms of this license.

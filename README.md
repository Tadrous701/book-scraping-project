# Book Data Web Scraping Project

## Overview
This project scrapes book information from [BooksToScrape.com](http://books.toscrape.com) using Python.  
It extracts book title, price, rating, availability, and product page links, then exports the data to a CSV file for easy analysis.

## Features
- Scrapes multiple pages with pagination
- Extracts the following fields:
  - Title
  - Price
  - Rating
  - Availability
  - Product Page URL
- Clean CSV output
- Polite scraping using delays to avoid server overload

## Tools & Skills
- Python
- Requests
- BeautifulSoup
- CSV handling
- Data extraction

## Files
- `book_scraper.py` – Python script for scraping
- `books.csv` – Exported data
- `Book_Scraping_Portfolio.pdf` – Portfolio PDF with screenshots and process explanation

## How to Use
1. Clone this repository:  
   `git clone <repository_url>`
2. Install dependencies:  
   `pip install requests beautifulsoup4`
3. Run the scraper:  
   `python book_scraper.py`
4. The data will be saved in `books.csv`

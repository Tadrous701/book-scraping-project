import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# prepare CSV file
with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Availability", "Rating", "URL"])

    # loop through 50 pages
    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Page {page} not found, stopping.")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            
            # rating is in class attribute like "star-rating Three"
            rating_class = book.find("p")["class"]
            rating = rating_class[1] if len(rating_class) > 1 else "N/A"
            
            link = "http://books.toscrape.com/catalogue/" + book.h3.a["href"]
            
            writer.writerow([title, price, availability, rating, link])
        
        print(f"Scraped page {page}")


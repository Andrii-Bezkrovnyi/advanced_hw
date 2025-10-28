import csv

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/page-1.html"
PAGES_NUMBER = 3  # Limit of pages to avoid infinite loop

books = []

for _ in range(PAGES_NUMBER):
    print(f"Scraping: {URL}")
    response = requests.get(URL)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # Analysis of the page
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        # Book title
        title = article.h3.a["title"]

        # Book price
        price = article.find("p", class_="price_color").text.strip().lstrip("£")

        # Book rating
        rating = article.find("p", class_="star-rating")["class"][1]

        # Book availability
        availability = True if "In stock" in article.find(
            "p",
            class_="instock availability"
        ).text.strip() else False

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    # Check for next page
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page = next_btn.a["href"]
        URL = "https://books.toscrape.com/catalogue/" + next_page
    else:
        break

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Price", "Rating", "Availability"])
    writer.writeheader()
    writer.writerows(books)

print(f"Save {len(books)} Books into 'books.csv'")

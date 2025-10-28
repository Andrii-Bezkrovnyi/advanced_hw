import requests
from bs4 import BeautifulSoup

url = "https://www.sheldonbrown.com/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

title = soup.title.string
print("Title:", title)

divs = soup.find_all("div")
print(f"Founded {len(divs)} <div> tags:")
for tag_index, div in enumerate(divs, 1):
    print(f"{tag_index}. {div}")

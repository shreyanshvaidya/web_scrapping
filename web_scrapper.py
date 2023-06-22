import requests
from bs4 import BeautifulSoup

url_link = input("Enter the URL Link: ")

result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

finds = doc.find_all("a")
for find in finds:
    href = find.get("href")
    print(href)

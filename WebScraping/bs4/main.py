from bs4 import BeautifulSoup


with open("website.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all(name="a")

for tag in tags:
    print(tag.get("href"))
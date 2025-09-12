from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
data = response.text
soup = BeautifulSoup(data, "html.parser")

titles = [title.getText() for title in soup.find_all(name="span", class_="titleline")]
links = [link.get("href") for link in soup.select(".titleline > a")]
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(titles)
print(links)
print(scores)
import requests
from bs4 import BeautifulSoup

url = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=wonderwall'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.content, 'xml')
# print(soup)
print(soup.text)
print(soup.find("Artist").text)
print(soup.find("Song").text)
print(soup.find("SongRank").text)
print(soup.find("SearchLyricResult").find("ArtistUrl").text)
print(len(soup.findAll("SearchLyricResult")))


url = "http://mignews.com/mobile"
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
news = soup.findAll("title")
print(soup.find("body").text)
print(soup.findAll("div"))

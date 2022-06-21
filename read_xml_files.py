import requests
from bs4 import BeautifulSoup

url = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=wonderwall'
web = requests.get(url)
soup = BeautifulSoup(web.content, 'xml')
# print(soup)
print(soup.find("Artist").text)
print(soup.find("Song").text)
print(soup.find("SongRank").text)
print(soup.find("SearchLyricResult").find("ArtistUrl").text)
print(len(soup.findAll("SearchLyricResult")))



import requests
from bs4 import BeautifulSoup

url = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=wonderwall'
web = requests.get(url)
soup = BeautifulSoup(web.content, 'xml')
print(soup)



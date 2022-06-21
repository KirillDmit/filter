import requests
from bs4 import BeautifulSoup

cities = dict()
cities["Taipei"] = "https://weather.com/en-GB/weather/today/l" \
                   "/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d "

city = input()
url = cities[city]
page_request = requests.get(url)
soup = BeautifulSoup(page_request.content, 'html.parser')
print(soup.find('span', {'data-tested': 'TemperatureValue'}).text)



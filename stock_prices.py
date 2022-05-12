import sys
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6 import QtCore

import requests
from bs4 import BeautifulSoup

# first tell requests to get the webpage info
URL = "https://www.marketwatch.com/investing/stock/gme"
web = requests.get(URL)
soup = BeautifulSoup(web.content, 'html.parser')
#print(soup.prettify())
print(soup.findAll('h1'))
print(soup.find('h1', {'class': 'company__name'}))
price = soup.find('bg-quote', {'format': '0,0.00', 'field': 'Last'})
percent = soup.find('bg-quote', {'format': '0,0.00%', 'session': 'after'})
print(price)
print(percent)

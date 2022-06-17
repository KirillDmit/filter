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
# print(soup.prettify())
print(soup.findAll('h1'))
print(soup.find('h1', {'class': 'company__name'}))
price = soup.find('bg-quote', {'format': '0,0.00', 'field': 'Last'})
percent = soup.find('bg-quote', {'format': '0,0.00%', 'session': 'after'})
print(price)
print(percent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Stock prices"
        self.setWindowTitle(self.title)

        main_layout = QVBoxLayout()

        current_price = QLabel(price)
        current_price.setFont(QFont('Arial', 40))
        current_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(current_price)

        reaction = QLabel(self)
        stonks = QPixmap('stonks.png')
        not_stonks = QPixmap('not_stonks.png')
        if percent[0] == "-":
            reaction.setPixmap(not_stonks)
        else:
            reaction.setPixmap(stonks)

        main_layout.addWidget(reaction)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

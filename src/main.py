#
# Created in 2020 by Jake Johnson and Preston Windfeldt
# Filename: main.py
# Purpose:  Main program that constantly checks if mountain
#           reservations become available on the Ikon pass.
#

import sys
import ikonScraperInterface
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from PyQt5.QtCore import QDateTime, Qt, QTimer, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QLabel,
        QPushButton, QWidget, QDialog, QGridLayout, QGroupBox, QHBoxLayout,
        QVBoxLayout)

# MACRO for if web driver should run in headless mode or not
# Must be set to 1 if running on virtual server
HEADLESS = 0

class WidgetGallery(QDialog):
	def __init__(self, parent=None):
		super(WidgetGallery, self).__init__(parent)

		mainLayout = QVBoxLayout()
		startBotButton = QPushButton("Start")
		startBotButton.clicked.connect(self.startBot)
		mainLayout.addWidget(startBotButton)


		self.setLayout(mainLayout)
		self.setWindowTitle("Ikon Bot")

	@pyqtSlot()
	def startBot(self):
		startBot()


def startBot():	
	"""Main function. initializes web driver, logs into ikon site,
	and runs an infinite loop checking for openings of dates specified
	by user.
	"""

	# list to store dates to reserve
	datesToReserve = []
	# list to store available dates
	availableDates = []

	# initialize web driver
	if (HEADLESS):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		options.add_argument("window-size=1024,768")
		options.add_argument("--no-sandbox")
		options.add_argument("--log-level=3");
		driver = webdriver.Chrome(options=options)
	else:
		driver = webdriver.Chrome()

	# set page load timeout
	driver.set_page_load_timeout(20)

	# login to ikon website
	ikonScraperInterface.login(driver)

	# fill up dates lists
	ikonScraperInterface.addAvailableDatesToList(driver, availableDates)
	ikonScraperInterface.addDatesToReserveToList(datesToReserve)

	# Constantly check for openings in reservations
	while(True):
		ikonScraperInterface.checkForOpenings(driver, availableDates, datesToReserve)
		print("Still checking")

		# sleep so CPU processing doesn't get taken up
		time.sleep(2)

	# close driver
	driver.quit()

	# quit app
	sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()

    sys.exit(app.exec_()) 

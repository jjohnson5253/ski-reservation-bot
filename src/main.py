#
# Copyright 2020 Jake Johnson and Preston Windfeldt
# Filename: main.py
# Purpose:  Main program that constantly checks if mountain
#           reservations become available on the Ikon pass.
#

import sys
import ikonScraperInterface
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# MACRO for if web driver should run in headless mode or not
# Must be set to 1 if running on virtual server
HEADLESS = 1

def main():	
	"""Main function. TODO: update with what it does
	"""
	# initialize web driver
	if (HEADLESS):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		options.add_argument("window-size=1024,768")
		options.add_argument("--no-sandbox")
		#options.add_argument("--disable-logging")
		options.add_argument("--log-level=3");
		driver = webdriver.Chrome(options=options)
	else:
		driver = webdriver.Chrome()

	# login to ikon website
	ikonScraperInterface.login(driver)

	# list to store available dates
	availableDates = []

	# fill up list
	ikonScraperInterface.addAvailableDatesToList(driver, availableDates)

	# Constantly check for openings in reservations
	while(True):
		ikonScraperInterface.checkForOpenings(driver, availableDates)
		print("Still checking")
		time.sleep(2)

	# close driver
	driver.quit()

	# quit app
	sys.exit()

if __name__ == "__main__":
    main()
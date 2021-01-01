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
HEADLESS = 0

def main():	
	"""Main function. TODO: update with what it does
	"""
	# get user input for date and password
	pwInput = sys.argv[1]

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
	ikonScraperInterface.login(driver, pwInput)

	# fill up database with date availability
	ikonScraperInterface.addDatesToDB(driver)

	# Constantly check for openings and update database afterward
	while(1):
		ikonScraperInterface.checkForOpenings(driver)
		#ikonScraperInterface.addDatesToDB(driver)

		print("Still checking")

	# close driver
	driver.quit()

	# quit app
	sys.exit()
	
if __name__ == "__main__":
    main()
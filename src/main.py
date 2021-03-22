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

# MACRO for if web driver should run in headless mode or not
# Must be set to 1 if running on virtual server
HEADLESS = 0

def main():	
	"""Main function. initializes web driver, logs into ikon site,
	and runs an infinite loop checking for openings of dates specified
	by user.
	"""
	# list to store dates to reserve
	datesToReserve = []
	# list to store available dates
	availableDates = []
	# mountains to check for availability
	mountainsToCheck = []
	# dictionary to store which months to check. Gets updated.
	monthsToCheck = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June"
	}

	# initialize web driver
	if (HEADLESS):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		options.add_argument("window-size=1024,768")
		options.add_argument("--no-sandbox")
		options.add_argument("--log-level=3");
		driver = webdriver.Chrome(options=options)
		driver.set_window_position(0, 0)
		driver.set_window_size(1024, 768)
	else:
		driver = webdriver.Chrome()

	# set page load timeout
	driver.set_page_load_timeout(20)

	# login to ikon website
	ikonScraperInterface.login(driver)

	# remove months to check that have already been passed
	ikonScraperInterface.updateMonthsToCheck(monthsToCheck)

	# fill up dates lists
	ikonScraperInterface.addDatesToReserveToList(datesToReserve, mountainsToCheck)
	ikonScraperInterface.addAvailableDatesToList(driver, availableDates, mountainsToCheck, monthsToCheck)

	# Constantly check for openings in reservations
	while(True):
		ikonScraperInterface.checkForOpenings(driver, availableDates, datesToReserve, mountainsToCheck, monthsToCheck)
		print("Still checking")

		# sleep so CPU processing doesn't get taken up
		time.sleep(2)

	# close driver
	driver.quit()

	# quit app
	sys.exit()

if __name__ == "__main__":
    main()

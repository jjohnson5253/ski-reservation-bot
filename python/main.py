import sys
import ikonScraperInterface

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HEADLESS = 1

"""
def constantCheck():
	while(1):
		if (checkAvail.checkAvail(pwInput, monthInput, dayInput, yearInput) == true):
			# send email and/or make reservation
"""

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
		driver = webdriver.Chrome(chrome_options=options)
	else:
		driver = webdriver.Chrome()

	# login to ikon website
	ikonScraperInterface.login(driver, pwInput)

	# fill up database with date availability
	ikonScraperInterface.addDatesToDB(driver)

	# check for openings every minute
	while(1):
		ikonScraperInterface.checkForOpenings(driver)
		#time.sleep(60)

	# close driver
	driver.quit()

	# quit app
	sys.exit()
	

if __name__ == "__main__":
    main()
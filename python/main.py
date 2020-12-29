import sys
import ikonScrapeInterface

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
def constantCheck():
	while(1):
		if (checkAvail.checkAvail(pwInput, monthInput, dayInput, yearInput) == true):
			# send email and/or make reservation
"""

def main():
	# get user input for date and password
	pwInput = sys.argv[1]
	monthInput = sys.argv[2]
	dayInput = sys.argv[3]
	yearInput = sys.argv[4]

	# initialize web driver
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	options.add_argument("window-size=1024,768")
	options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(chrome_options=options)

	ikonScrapeInterface.login(driver, pwInput)

	ikonScrapeInterface.isAvailable(driver, monthInput, dayInput, yearInput)
	sys.exit()

if __name__ == "__main__":
    main()
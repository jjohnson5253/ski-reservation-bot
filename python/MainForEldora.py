import sys
import eldoraScraper

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
	monthInput = sys.argv[1]
	dayInput = sys.argv[2]
	timeInput = sys.argv[3]

	# initialize web driver
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	options.add_argument("window-size=1024,768")
	options.add_argument("--no-sandbox") 
	driver = webdriver.Chrome(chrome_options=options)

	eldoraScraper.login(driver)

	eldoraScraper.isAvailable(driver, monthInput, dayInput, timeInput)
	sys.exit()

if __name__ == "__main__":
	main()
# Created: 12/21/2020
# Author: Jake Johnson
# usage: py checkAvail [password] [month] [day] [year]

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class name if the day is available
AVAILABLE = 'DayPicker-Day'

def login(driver, password):
	# open login page
	url = "https://account.ikonpass.com/en/login"
	driver.get(url)

	# send login parameters
	username = driver.find_element_by_name('email')
	username.send_keys('jjohnson11096@gmail.com')
	password = driver.find_element_by_name('password')
	password.send_keys(sys.argv[1])
	password.send_keys(Keys.RETURN)

	# click 'Make a Reservation' button
	try:
		# wait for page to load
		resButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Make a Reservation"]')))
	except:
		print("Error: Timed out")
		sys.exit()
	# use a javascript click, the selenium click not working
	driver.execute_script("arguments[0].click();", resButton)

def isAvailable(driver, month, day, year):
	# select mountain
	try:
		# wait for page to load
		mountain = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Arapahoe Basin"]')))
	except:
		print("Error: Timed out")
		sys.exit()
	mountain.click();

	# click 'Continue' button
	try:
		# wait for page to load
		contButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Continue"]')))
	except:
		print("Error: Timed out")
		sys.exit()
	contButton.click()

	# check if correct month is being checked
	try:
		# wait for page to load
		monthBeingChecked = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
	except:
		print("Error: Timed out")
		sys.exit()

	# loop through months until correct month is being checked
	while (monthBeingChecked.get_attribute('innerHTML') != (month + ' ' + year)):
		# go to next month
		nextMonthButton = driver.find_element(By.XPATH, '//i[@class="amp-icon icon-chevron-right"]')
		nextMonthButton.click()
		try:
			monthBeingChecked = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
		except:
			print("Error: Timed out")
			sys.exit()

	# parse monthInput since that is how it is labeled in the Ikon page HTML
	month = month[0:3]

	# check if day is available by reading element class. Class will be 'DayPicker-Day'
	# if available
	try:
		# wait for page to load
		day = WebDriverWait(driver, 20).until(
	    EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"' + month + ' ' + day + '")]')))
	except:
		print("Error: Timed out")
		sys.exit()

	# print if day is available or not
	if (day.get_attribute('class') == AVAILABLE):
		print("This day is available")
		driver.quit()
		return True
	else:
		print("This day is not available")
		driver.quit()
		return False

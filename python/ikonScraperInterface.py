# Created: 12/21/2020
# Author: Jake Johnson
# usage: py checkAvail [password] [month] [day] [year]

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar
import time
#import mysql.connector

# class name if the day is available
AVAILABLE = 'DayPicker-Day'
# number of days in each month TODO: use monthrange instead from calendar lib
DAYS_IN_DECEMBER = 31
DAYS_IN_JANUARY = 31
DAYS_IN_FEBRUARY = 28
DAYS_IN_MARCH = 31
DAYS_IN_APRIL = 30
DAYS_IN_MAY = 31

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

def selectMountain(driver, mountain):
	# select mountain
	try:
		# wait for page to load
		mountain = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="' + mountain + '"]')))
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

def selectMonth(driver, month, year):
	print("selecting: " + month)

	# check what month is currently being checked on Ikon site.
	try:
		# wait for page to load
		monthBeingChecked = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
	except:
		print("Error: Timed out")
		sys.exit()

	print ("month being checked: " + monthBeingChecked.get_attribute('innerHTML'))

	# loop through months until correct month is being checked. 
	# Will start from month entered and increment until June 2021.
	while (monthBeingChecked.get_attribute('innerHTML') != (month + ' ' + str(year))):
		print("month being checked in loop: " + monthBeingChecked.get_attribute('innerHTML'))
		print("month inputted:              " + month + ' ' + str(year))

		# if we have reached June and that was not desired month, return
		if monthBeingChecked.get_attribute('innerHTML') == ("June 2021") and month != "June":
			print("Error: Failed to select month")
			return

		# go to next month
		nextMonthButton = driver.find_element(By.XPATH, '//i[@class="amp-icon icon-chevron-right"]')
		nextMonthButton.click()
		
		try:
			monthBeingChecked = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
		except:
			print("Error: Timed out")
			sys.exit()

	print("month being checked in loop: " + monthBeingChecked.get_attribute('innerHTML'))
	print("month inputted:              " + month + ' ' + str(year))

def isAvailable(driver, month, day, year):
	# parse monthInput since that is how it is labeled in the Ikon page HTML
	month = month[0:3]

	# format day, if it's single digits, prepend with 0 since that is Ikon's site format
	dayFormatted = str(day)
	if (day < 10):
		dayFormatted = "0" + dayFormatted

	# check if day is available by reading element class. Class will be 'DayPicker-Day'
	# if available
	try:
		# wait for page to load
		dayElement = WebDriverWait(driver, 20).until(
	    EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"' + month + ' ' + dayFormatted + '")]')))
	except:
		print("Error: Timed out")
		#sys.exit()

	# print if day is available or not
	if (dayElement.get_attribute('class') == AVAILABLE):
		print("This day is available")
		return True
	else:
		print("This day is not available")
		return False

def addReservedDatesToDB(driver):
	monthsToCheck = {
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June"
	}
	months = [1,2,3,4,5,6]
	year = 2021

	"""
	# connect to database
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="yourmom",
	  password="Yourmom123!"
	)
	mycursor = mydb.cursor()
	"""
	"""
	mycursor.execute("INSERT INTO reservationchecks(mountain, month, day, year, email) 
		VALUES ('".$_POST["mountain"]."','".$_POST["month"]."','".$_POST["day"]."',
			'".$_POST["year"]."','".$_POST["email"]."')"")
	"""

	# check reserved dates. Only check Jan-June 
	# TODO: make this scalable to whatever current year is
	for month in monthsToCheck:
		# select month to check on ikon site
		selectMonth(driver, monthsToCheck[month], year)
		# check each days availability
		for day in range(1, calendar.monthrange(year, month)[1] + 1):
			print (str(month) + " " + str(day))
			isAvailable(driver, monthsToCheck[month], day, year)





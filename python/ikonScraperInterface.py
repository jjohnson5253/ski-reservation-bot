#
# Copyright 2020 Jake Johnson and Preston Windfeldt
# Filename: ikonScraperInterface.py
# Purpose:  Provide web scraping interface for interacting with 
#           Ikon website
#

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import smtplib
import emailInterface

# class name if the day is available
AVAILABLE = 'DayPicker-Day'
# class name if available and day is today
AVAILABLE_TODAY = 'DayPicker-Day DayPicker-Day--today'

# mountains to check for availability
mountainsToCheck = ["Arapahoe Basin", "Aspen Snowmass", "Winter Park Resort"]
# months to check for availability
monthsToCheck = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June"
}
# year to check
year = 2021

def login(driver, password):
	"""Logs into Ikon website and clicks the 'make reservation' button.
	"""
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
	"""Selects mountain on the 'make reservation' page. From here, selectMonth() and
	then isDayAvailable() can be called.
	"""
	# select mountain
	try:
		# wait for page to load
		mountain = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="' + mountain + '"]')))
	except:
		print("Error: Timed out")
		sys.exit()
	driver.execute_script("arguments[0].click();", mountain)

	# click 'Continue' button
	try:
		# wait for page to load
		contButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Continue"]')))
	except:
		print("Error: Timed out")
		sys.exit()
	driver.execute_script("arguments[0].click();", contButton)

def selectMonth(driver, month, year):
	"""Selects month by bringing scraper to the page displaying the dates for that
	month.
	"""
	# check what month is currently being checked on Ikon site.
	try:
		# wait for page to load
		monthBeingChecked = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
	except:
		print("Error: Timed out")
		sys.exit()

	# loop through months until correct month is being checked. 
	# Will start from month entered and increment until June 2021.
	while (monthBeingChecked.get_attribute('innerHTML') != (month + ' ' + str(year))):
		# if we have reached June and that was not desired month, return
		if monthBeingChecked.get_attribute('innerHTML') == ("June 2021") and month != "June":
			print("Error: Failed to select month")
			return

		# go to next month
		nextMonthButton = driver.find_element(By.XPATH, '//i[@class="amp-icon icon-chevron-right"]')
		driver.execute_script("arguments[0].click();", nextMonthButton)

		try:
			monthBeingChecked = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
		except:
			print("Error: Timed out")
			sys.exit()

def isDayAvailable(driver, month, day, year):
	"""Checks if a day is available. The scraper must be on the make reservation
	page with the dates available to check (ie selectMonth() must be called first).
	"""
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

	if month == "Jan" and day == 1:
		print(dayElement.get_attribute('class'))

	# print if day is available or not
	if (dayElement.get_attribute('class') == AVAILABLE or dayElement.get_attribute('class') == AVAILABLE_TODAY):
		#print(month + " " + dayFormatted + " AVAILABLE")
		return True
	else:
		#print(month + " " + dayFormatted + " RESERVED")
		return False

def addDatesToDB(driver):
	"""Adds all reserved dates to the datesreserved table and all available
	dates to the datesavailable table in the mtnrez MYSQL database.
	"""

	# connect to database
	db = mysql.connector.connect(
	  host="localhost",
	  user="yourmom",
	  password="Yourmom123!",
	  database="mtnrez"
	)
	cursor = db.cursor(buffered = True)

	# clear tables first
	sql = "DELETE FROM datesavailable"
	cursor.execute(sql)
	sql = "DELETE FROM datesreserved"
	cursor.execute(sql)

	# check reserved dates for each mountain. Only check Jan-June 
	# TODO: make this scalable to whatever current year is
	for mountain in mountainsToCheck:
		# reload to allow new mountain selection
		url = "https://account.ikonpass.com/en/myaccount/add-reservations/"
		driver.get(url)
		selectMountain(driver, mountain)
		for month in monthsToCheck:
			selectMonth(driver, monthsToCheck[month], year)
			# check each days availability and insert into database tables
			for day in range(1, calendar.monthrange(year, month)[1] + 1):
				if isDayAvailable(driver, monthsToCheck[month], day, year):
					sql = "INSERT INTO datesavailable(mountain, month, day, year) VALUES (%s, %s, %s, %s)"
					vals = (mountain, monthsToCheck[month], str(day), str(year))
					cursor.execute(sql, vals)

	db.commit()
	cursor.close()

def checkForOpenings(driver):
	"""Checks if any reserved days have become open by scraping Ikon site and comparing
	to the current stored reserved days in our database
	"""
	
	# connect to database
	db = mysql.connector.connect(
	  host="localhost",
	  user="yourmom",
	  password="Yourmom123!",
	  database="mtnrez"
	)
	cursor = db.cursor(buffered = True)

	# check current available dates to see if they weren't available in database
	for mountain in mountainsToCheck:
		# reload to allow new mountain selection
		url = "https://account.ikonpass.com/en/myaccount/add-reservations/"
		driver.get(url)
		selectMountain(driver, mountain)
		for month in monthsToCheck:
			selectMonth(driver, monthsToCheck[month], year)
			# check each days availability and insert into database tables
			for day in range(1, calendar.monthrange(year, month)[1] + 1):
				if isDayAvailable(driver, monthsToCheck[month], day, year):
					# check if this day is in the database already as available
					sql = "SELECT * FROM datesavailable WHERE (mountain, month, day, year) = (%s, %s, %s, %s)"
					vals = (mountain, monthsToCheck[month], str(day), str(year))
					cursor.execute(sql, vals)
					# if not, insert into db send email alert
					if cursor.rowcount == 0:
						print("This day just became available!!!")
						print(str(month) + " " + str(day))

						sql = "INSERT INTO datesavailable(mountain, month, day, year) VALUES (%s, %s, %s, %s)"
						vals = (mountain, monthsToCheck[month], str(day), str(year))
						cursor.execute(sql, vals)

						emailInterface.sendEmailAlert("jjohnson11096@gmail.com", mountain, monthsToCheck[month], str(day), str(year))
						#############################emailInterface.sendEmailAlert("prestonwindfeldt@gmail.com", mountain, monthsToCheck[month], str(day), str(year))
				else:
					# if not available, check if this day is in the database as available
					sql = "SELECT * FROM datesavailable WHERE (mountain, month, day, year) = (%s, %s, %s, %s)"
					vals = (mountain, monthsToCheck[month], str(day), str(year))
					cursor.execute(sql, vals)
					# if it is, delete it
					if cursor.rowcount != 0:
						sql = "DELETE FROM datesavailable WHERE mountain = %s AND month =%s AND day = %s AND year = %s"
						vals = (mountain, monthsToCheck[month], str(day), str(year))
						cursor.execute(sql, vals)					

	db.commit()
	cursor.close()
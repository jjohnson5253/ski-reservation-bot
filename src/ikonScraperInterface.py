#
# Created in 2020 by Jake Johnson and Preston Windfeldt
# Filename: ikonScraperInterface.py
# Purpose:  Provide web scraping interface for interacting with 
#           Ikon website
#

import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import calendar
import smtplib
import emailInterface
import time
import datetime

# class name if the day is available
AVAILABLE = 'DayPicker-Day'
# class name if available and day is today
AVAILABLE_TODAY = 'DayPicker-Day DayPicker-Day--today'
# mountains to check for availability
mountainsToCheck = ["Arapahoe Basin", "Winter Park Resort"]
# months to check for availability
monthsToCheck = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June"
}
# dict to store index of day/month/year in each line of datesToReserve
# txt file
datesTxtFileIndex = {'day':0, 'month':1, 'year':2}
# year to check
year = 2021
# Ikon account email
ikonEmail = sys.argv[1]
# macro for if user wants all mountain openings to be emailed to them.
# Not just ones in their dates to reserve.
ALERT_ALL_OPENINGS = False
# url to the make reservation page
makeResUrl = "https://account.ikonpass.com/en/myaccount/add-reservations/"

def login(driver):
	"""Logs into Ikon website and clicks the 'make reservation' button.
	"""
	# open login page
	url = "https://account.ikonpass.com/en/login"
	driver.get(url)
	
	# send login parameters
	username = driver.find_element_by_name('email')
	username.send_keys(sys.argv[1])
	password = driver.find_element_by_name('password')
	password.send_keys(sys.argv[2])
	password.send_keys(Keys.RETURN)

	# click 'Make a Reservation' button
	try:
		# wait for page to load
		resButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Make a Reservation"]')))
	except:
		print("Error: Timed out")
		emailInterface.sendErrorEmail("Error logging in", ikonEmail)
		sys.exit()
	driver.execute_script("arguments[0].click();", resButton)

def selectMountain(driver, mountain):
	"""Selects mountain on the 'make reservation' page. From here, selectMonth() 
	and then isDayAvailable() can be called.
	"""
	# select mountain
	try:
		# wait for page to load
		mountain = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="' + mountain + '"]')))
	except:
		print("Error: Timed out")
		emailInterface.sendErrorEmail("Error selecting mountain " + mountain, ikonEmail)
		sys.exit()
	driver.execute_script("arguments[0].click();", mountain)

	# click 'Continue' button
	try:
		# wait for page to load
		contButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Continue"]')))
	except:
		print("Error: Timed out")
		emailInterface.sendErrorEmail("Error selecting mountain " + mountain, ikonEmail)
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
		EC.presence_of_element_located((By.XPATH, '//span[@class="sc-qPyvj jTgFdL"]')))
	except:
		print("Error: Timed out")
		emailInterface.sendErrorEmail("Error selecting month " + month, ikonEmail)		
		sys.exit()

	# loop through months until correct month is being checked. 
	# Will start from month entered and increment until June 2021.
	while (monthBeingChecked.get_attribute('innerHTML') != 
        (month + ' ' + str(year))):
		# if we have reached June and that was not desired month, return
		if monthBeingChecked.get_attribute('innerHTML') == ("June 2021") and month != "June":
			print("Error: Failed to select month")
			return

		# go to next month
		nextMonthButton = driver.find_element(By.XPATH, '//i[@class="amp-icon icon-chevron-right"]')
		driver.execute_script("arguments[0].click();", nextMonthButton)

		try:
			monthBeingChecked = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//span[@class="sc-qPyvj jTgFdL"]')))
		except:
			print("Error: Timed out")
			emailInterface.sendErrorEmail("Error selecting month " + month, ikonEmail)
			sys.exit()

def isDayAvailable(driver, month, day, year):
	"""Checks if a day is available. The scraper must be on the make reservation
	page with the dates available to check (ie selectMonth() must be called first).
	"""
	# parse monthInput since that is how it is labeled in the Ikon page HTML
	month = month[0:3]

	# format day, if it's single digits, prepend with 0 since that is Ikon's
	# site format
	dayFormatted = str(day)
	if (day < 10):
		dayFormatted = "0" + dayFormatted

	# check if day is available by reading element class. Class will be 
	# 'DayPicker-Day' if available
	try:
		# wait for page to load
		dayElement = WebDriverWait(driver, 20).until(
	    EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"' + month + ' ' + dayFormatted + '")]')))
	except:
		print("Error: Timed out")
		emailInterface.sendErrorEmail("Error checking day availability for " + month + " " + day, ikonEmail)
		sys.exit()

	# return if day is available or not
	if (dayElement.get_attribute('class') == AVAILABLE or dayElement.get_attribute('class') == AVAILABLE_TODAY):
		return True
	else:
		return False

def addDatesToReserveToList(datesToReserve):
	# get path to datesToReserve file. Should be in current directory
	# todo: fix this... it is currently making "/datesToReserve.txt" when
	# it should make "datesToReserve.txt"
	path = os.path.join(os.getcwd(), "datesToReserve.txt")

	# open file and add contents to list
	datesTxtFile = open(path)
	for date in datesTxtFile:
		date = date.split()
		datesToReserve.append([date[datesTxtFileIndex['day']], date[datesTxtFileIndex['month']], date[datesTxtFileIndex['year']]])

def addAvailableDatesToList(driver, datesAvailable):
	"""Scrapes Ikon site and adds available dates to list.
	"""
	# check reserved dates for each mountain. Only check Jan-June 
	# TODO: make this scalable to whatever current year is
	for mountain in mountainsToCheck:
		# reload to allow new mountain selection
		driver.get(makeResUrl)
		selectMountain(driver, mountain)
		for month in monthsToCheck:
			selectMonth(driver, monthsToCheck[month], year)
			# check each days availability and add to list
			for day in range(1, calendar.monthrange(year, month)[1] + 1):
				if isDayAvailable(driver, monthsToCheck[month], day, year):
					datesAvailable.append([mountain, month, day, year])

def checkForOpenings(driver, datesAvailable, datesToReserve):
	"""Checks if any reserved days have become available by scraping Ikon site 
	and comparing to the current stored available dates in our list. Reserves 
	days that are set in database if they become available.
	"""
	# check current available dates
	for mountain in mountainsToCheck:
		# reload to allow new mountain selection
		url = "https://account.ikonpass.com/en/myaccount/add-reservations/"
		driver.get(url)
		selectMountain(driver, mountain)

		for month in monthsToCheck:
			selectMonth(driver, monthsToCheck[month], year)

			for day in range(1, calendar.monthrange(year, month)[1] + 1):
				if isDayAvailable(driver, monthsToCheck[month], day, year):
					# check if date is in datesToReserve and reserve if so
					if [str(month), str(day), str(year)] in datesToReserve:
						reserveDay(driver, monthsToCheck[month], day, year, mountain)
						# return to make reservation page
						driver.get(makeResUrl)
						# get day of week
						dayOfWeek = datetime.date(year, month, day).strftime("%A")
						# send alert
						emailInterface.sendDateToReserveAlertEmail(ikonEmail, mountain, monthsToCheck[month], str(day), str(year), dayOfWeek, ikonEmail)
						# refresh scraper
						selectMountain(driver, mountain)
						selectMonth(driver, monthsToCheck[month], year)

					# if day is not stored as available send alert if desire and
					# add to available dates
					if [mountain, month, day, year] not in datesAvailable:
						# get day of week
						dayOfWeek = datetime.date(year, month, day).strftime("%A")
						# send alerts if desired
						if ALERT_ALL_OPENINGS:
							emailInterface.sendReservationOpenAlertEmail(ikonEmail, mountain, monthsToCheck[month], str(day), str(year), dayOfWeek, ikonEmail)
						# add to list
						datesAvailable.append([mountain, month, day, year])
				else:
					# if day is not available but stored as available, remove it 
					# from list
					if [mountain, month, day, year] in datesAvailable:
						datesAvailable.remove([mountain, month, day, year])

def reserveDay(driver, month, day, year, mountain):
	"""Reserves a day in Ikon if available.
	"""
	# parse monthInput since that is how it is labeled in the Ikon page HTML
	month = month[0:3]

	# format day, if it's single digits, prepend with 0 since that is Ikon's 
	# site format
	dayFormatted = str(day)
	if (day < 10):
		dayFormatted = "0" + dayFormatted

	# Select the day
	# if available
	try:
		# wait for page to load
		dayElement = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"' + month + ' ' + dayFormatted + '")]')))
		driver.execute_script("arguments[0].click();", dayElement)
	except:
		emailInterface.sendErrorEmail("Error reserving " + mountain + " on "  + month + " " + str(day) + ", " + str(year), ikonEmail)
		return

	# click save button
	try:
		# wait for page to load
		saveButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Save"]')))
		driver.execute_script("arguments[0].click();", saveButton)
	except:
		emailInterface.sendErrorEmail("Error reserving " + mountain + " on " + month + " " + str(day) + ", " + str(year), ikonEmail)
		return

	# give time for button click
	time.sleep(1)

	# click confirm button
	try:
		# wait for page to load
		confirmButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[text()="Continue to Confirm"]')))
		driver.execute_script("arguments[0].click();", confirmButton)
	except:
		emailInterface.sendErrorEmail("Error reserving " + mountain + " on " + month + " " + str(day) + ", " + str(year), ikonEmail)
		return

	# give time for button click
	time.sleep(1)
	
	# click confirm checkbox
	try:
		# wait for page to load
		confirmCheckbox = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, 
            '//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[4]/div/div[4]/label/input')))
		driver.execute_script("arguments[0].click();", confirmCheckbox)
	except:
		emailInterface.sendErrorEmail("Error reserving " + mountain + " on " + month + " " + str(day) + ", " + str(year), ikonEmail)
		return

	# give time for button click
	time.sleep(1)

	# click confirm button again
	try:
		# wait for page to load
		confirmButton = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/section[2]/div/div[2]/div[4]/div/div[5]/button/span')))
		driver.execute_script("arguments[0].click();", confirmButton)
	except:
		emailInterface.sendErrorEmail("Error reserving " + mountain + " on " + month + " " + str(day) + ", " + str(year), ikonEmail)
		return

def checkSpecificReservation(driver, mountain, month, day, year):
	"""Checks for specific reservation and reserves if available
	"""
	# reload to allow new mountain selection
	driver.get(makeResUrl)

	selectMountain(driver, mountain)

	selectMonth(driver, monthsToCheck[month], year)

	if isDayAvailable(driver, monthsToCheck[month], day, year):
		# reserve day
		reserveDay(driver, monthsToCheck[month], day, year, mountain)
		# return to make reservation page
		driver.get(makeResUrl)
		# get day of week
		dayOfWeek = datetime.date(year, month, day).strftime("%A")
		# send alert
		emailInterface.sendDateToReserveAlertEmail(ikonEmail, mountain, monthsToCheck[month], str(day), str(year), dayOfWeek, ikonEmail)

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

def login(driver):
	# open login page
	url = "https://www.eldora.com/plan-your-trip/getting-here/parking-reservations"
	driver.get(url)


def isAvailable(driver, month, day, time):
	
	# check if correct month and year is being checked in the format Month(in words) Year(####)
	try:
		print("here")
		# wait for page to load
		monthBeingChecked = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//div[@class, "CalendarMonth_caption CalendarMonth_caption_1")]')))
	except:
		print("Error: Timed out")
		sys.exit()

	# loop through months until correct month is being checked
	while (monthBeingChecked.get_attribute('innerHTML') != (month + ' ' + "2021")):
		# go to next month
		print("hello")
		nextMonthButton = driver.find_element(By.XPATH, '//i[@class="iconified-font iconified-chevron-right"></span>]')
		nextMonthButton.click()   
		try:
			monthBeingChecked = WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//span[<div class="CalendarMonth_caption CalendarMonth_caption_1">]')))   
		except:
			print("Error: Timed out")
			sys.exit()
"""
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
"""
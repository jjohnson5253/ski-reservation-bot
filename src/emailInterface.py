# Copyright 2021 Jake Johnson and Preston Windfeldt

import smtplib

def sendEmailAlert(toAddress, mountain, month, day, year, dayOfWeek):
	"""Sends an email using smtp.
	"""
	FROMADDR = "mtnrezalert@gmail.com"
	PASSWORD = "wakeupsheeple123!"
	TOADDRS  = [toAddress]
	SUBJECT  = "A Reservation Has Become Available!"

	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
	msg += mountain + " on " + dayOfWeek + " " + month + " " + day + ", " + year + " opened up!!!\r\n"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(FROMADDR, PASSWORD)
	server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()

def sendErrorEmail(error):
	"""Sends an email to me notifying the program experienced an error
	"""
	FROMADDR = "mtnrezalert@gmail.com"
	PASSWORD = "wakeupsheeple123!"
	TOADDRS  = ["jjohnson11096@gmail.com"]
	SUBJECT  = "Error occurred on server!"

	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
	msg += "Error: " + error + "\r\n"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(FROMADDR, PASSWORD)
	server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()
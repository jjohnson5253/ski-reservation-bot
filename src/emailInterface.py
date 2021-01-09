# Created 2021 Jake Johnson and Preston Windfeldt

import smtplib

FROMADDR = "mtnrezalert@gmail.com"
PASSWORD = "wakeupsheeple123!"
	
def sendReservationOpenAlertEmail(toAddress, mountain, month, day, year, dayOfWeek, email):
	"""Sends an email using smtp.
	"""
	TOADDRS  = [toAddress]
	SUBJECT  = "A Reservation Has Become Available!"

	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
	msg += mountain + " on " + dayOfWeek + " " + month + " " + day + ", " + year + " opened up for " + email + "!!!\r\n"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(FROMADDR, PASSWORD)
	server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()

def sendDateToReserveAlertEmail(toAddress, mountain, month, day, year, dayOfWeek, email):
	"""Sends an email using smtp.
	"""
	TOADDRS  = [toAddress]
	SUBJECT  = "A Date To Reserve Reservation Has Become Available!"

	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
	msg += mountain + " on " + dayOfWeek + " " + month + " " + day + ", " + year + " opened up for " + email + "!!!\r\n"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(FROMADDR, PASSWORD)
	server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()

def sendErrorEmail(error, email):
	"""Sends an email to me notifying the program experienced an error
	"""
	TOADDRS  = [email]
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

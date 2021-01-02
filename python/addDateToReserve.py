# Copyright 2021 Jake Johnson

import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# get inputs
month = sys.argv[1]
day = sys.argv[2]
year = sys.argv[3]

# connect to database
db = mysql.connector.connect( host="localhost", user="yourmom", 
	 password="Yourmom123!", database="mtnrez")
cursor = db.cursor(buffered = True)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (month, day, year)
cursor.execute(sql, vals)

# commit and close connection
db.commit()
cursor.close()
# Copyright 2021 Jake Johnson

import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# SQL username
SQL_USERNAME = "reserver"
# SQL password
SQL_PASSWORD = "PurpleNapkin111$"
# SQL database
SQL_DB = "mtnrez"
# SQL host
SQL_HOST = "localhost"

# get inputs
month = sys.argv[1]
day = sys.argv[2]
year = sys.argv[3]
mountains = ""
if len(sys.argv) >= 5:
  mountains = sys.argv[4]
emails = ""
if len(sys.argv) >= 6:
  emails = sys.argv[5]

# connect to database
db = mysql.connector.connect( host=SQL_HOST, user=SQL_USERNAME, 
	 password=SQL_PASSWORD, database=SQL_DB)
cursor = db.cursor(buffered = True)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year, mountains, emails) VALUES (%s, %s, %s, %s, %s)"
vals = (month, day, year, mountains, emails)
cursor.execute(sql, vals)

# commit and close connection
db.commit()
cursor.close()
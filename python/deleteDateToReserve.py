# Copyright 2021 Jake Johnson

import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# SQL username
SQL_USERNAME = "reserver"
# SQL password
SQL_PASSWORD = "PurpleNapkin*^"
# SQL database
SQL_DB = "mtnrez"
# SQL host
SQL_HOST = "localhost"

# get inputs
month = sys.argv[1]
day = sys.argv[2]
year = sys.argv[3]

# connect to database
db = mysql.connector.connect( host="SQL_HOST", user="SQL_USERNAME", 
	 password="SQL_PASSWORD", database="SQL_DB")
cursor = db.cursor(buffered = True)

# add to database
sql = "DELETE FROM datesToReserve WHERE month = %s AND day = %s AND year = %s"
vals = (month, day, year)
cursor.execute(sql, vals)

# commit and close connection
db.commit()
cursor.close()
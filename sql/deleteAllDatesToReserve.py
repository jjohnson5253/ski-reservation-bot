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

# connect to database
db = mysql.connector.connect( host=SQL_HOST, user=SQL_USERNAME, 
	 password=SQL_PASSWORD, database=SQL_DB)
cursor = db.cursor(buffered = True)

# add to database
sql = "TRUNCATE datesToReserve"
cursor.execute(sql)

# commit and close connection
db.commit()
cursor.close()
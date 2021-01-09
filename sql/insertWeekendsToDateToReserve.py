# Created 2021 by Jake Johnson

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
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 9, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 10, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 16, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 17, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 23, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 24, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 30, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (1, 31, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 6, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 7, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 13, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 14, 2021)
cursor.execute(sql, vals)

# only check up to here for now
"""
# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 20, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 21, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 27, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (2, 28, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 6, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 7, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 13, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 14, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 20, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 21, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 27, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (3, 28, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 3, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 4, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 10, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 11, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 17, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 18, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 24, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (4, 25, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 1, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 2, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 8, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 9, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 15, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 16, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 22, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 23, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 29, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (5, 30, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 5, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 6, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 12, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 13, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 19, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 20, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 26, 2021)
cursor.execute(sql, vals)

# add to database
sql = "INSERT INTO datesToReserve(month, day, year) VALUES (%s, %s, %s)"
vals = (6, 27, 2021)
cursor.execute(sql, vals)
"""

# commit and close connection
db.commit()
cursor.close()
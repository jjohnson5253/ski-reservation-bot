import sys
import os
from enum import Enum

datesTxtFileIndex = {'day':0, 'month':1, 'year':2}

datesToReserve = []

filepath = 'datesToReserve.txt'
f = open(filepath)
for date in f:
	date = date.split()
	datesToReserve.append([date[datesTxtFileIndex['day']], date[datesTxtFileIndex['month']], date[datesTxtFileIndex['year']]])
	#print(date[datesTxtFileIndex['day']])
	#print(date[0])

for i in datesToReserve:
	print(i)
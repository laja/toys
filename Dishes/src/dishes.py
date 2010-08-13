#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.rrule import rrule, DAILY

# the people who can be used for some work :)
NAMES = ["András", "Benno", "Bogdán", "Gergely", "Lajos", "Krisztián"]

# the index of the person who should be the first to pick
# (indexing starts from zero as usual)
STARTING_INDEX = 3

# this is the interval we use to generate the schedule
START_DATE = date(2010,8,2)
END_DATE = date(2010,8,28)

# the official public holidays for the year
HOLIDAYS = [date(2010,8,20), date(2010,10,23), date(2010,11,1), date(2010,12,25), date(2010,12,26)]

def isWeekend(day):
	if day.weekday() == 5 or day.weekday() == 6:
		return True
	return False
	
def printThisDayAndName(day, name):
	print "|-"
	print "| " + day.strftime("%A %e %B %Y")
	print "| " + name

if __name__ == "__main__":
	rr = rrule(DAILY, dtstart=START_DATE, until=END_DATE)
	i = STARTING_INDEX
	for day in list(rr):
		if isWeekend(day) or day in HOLIDAYS: 
			continue
		printThisDayAndName(day, NAMES[i])
		i = i + 1
		if i == len(NAMES): 
			i = 0
		

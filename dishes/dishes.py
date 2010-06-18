#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.rrule import rrule, DAILY

NAMES = ["András", "Benno", "Bogdán", "Lajos", "Lóránt", "Krisztián", "Thomas"]
HOLIDAYS = [date(2010,05,24)]

startDate = date(2010,06,01)
endDate = date(2010,06,20)

def isWeekend(date):
	#if date.
	pass

if __name__ == "__main__":
	rr = rrule(DAILY, dtstart=startDate, until=endDate)
	i = 0
	for day in list(rr):
		if day.weekday() == 5 or day.weekday() == 6: continue
		print "|-"
		print "| " + str(day)
		print "| " + NAMES[i]
		i = i + 1
		if i == len(NAMES): i = 0
		

	

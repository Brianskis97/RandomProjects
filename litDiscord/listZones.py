#! /bin/python

from datetime import datetime
from pytz import timezone
from pytz import all_timezones

for each in all_timezones:
	print(each)


test={}
for i in range(len(all_timezones)):
	test[i] = ""

for i in range(len(all_timezones)):
        test[i//100] += all_timezones[i] + "\n"
print(test[0])

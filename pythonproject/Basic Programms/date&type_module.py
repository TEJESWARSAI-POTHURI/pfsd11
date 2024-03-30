#Date and Time Functions
import datetime
import time
print(time.time())
print(time.asctime())

sai=datetime.datetime.now()
print(sai)
print(sai.year)
print(sai.month)
print(sai.day)
print(sai.time())

'''
# Calendar Functions

import calendar
s=calendar.prcal(2004)

s2=calendar.month(2023,4)
s1=calendar.isleap(2005)
print(s1,s2,s)
'''

'''
from datetime import timedelta
x=datetime.datetime.now()
print(x+timedelta(days=-90))
'''

'''
import pytz
time1=pytz.timezone('Europe/Berlin')
print(datetime.datetime.now(time1))
'''
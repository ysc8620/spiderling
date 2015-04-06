__author__ = 'ShengYue'

from datetime import datetime, timedelta
import time
from math import log

epoch = datetime(1970, 1, 1)

def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def score(ups, downs):
    return ups - downs

def hot(ups,downs, date):
    """The hot formula. Should match the equivalent function in postgres."""
    #s = score(ups, downs)
    s = ups
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)

print hot(82,0,datetime(2002,05,01))
print hot(900,0,datetime(2014,05,02))
print hot(1020,0,datetime(2014,05,03))
print hot(1040,0,datetime(2014,05,04))
print hot(1020,0,datetime(2014,05,05))
print hot(1100,0,datetime(2014,05,06))
print hot(1020,0,datetime(2014,05,07))
print hot(1000,0,datetime(2014,05,8))


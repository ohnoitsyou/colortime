#!/usr/bin/env python3

import datetime

current = datetime.datetime.now()

print(current.second)


color = current.year - 2000 
color = color << 4 

color = color | current.month
color = color << 3 

color = color | current.day
color = color << 4

hour = current.hour
if hour % 12 == 0: 
  hour = 12
else: 
  hour = hour % 12 
color = color | hour 
color = color << 3 

color = color | current.minute
color = color << 5

color = color | current.second

print(format(color, '06x'))


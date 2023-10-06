from time import time, ctime, localtime
from datetime import datetime, timedelta,date

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

#Current Time :
import time
time = time.localtime(time.time())
print("Current local date and time is: ", time)

#Formatted Time :
import time
time = time.asctime(time.localtime(time.time()))
print ("Local current Date & Time:", time)

#Calender Month:
import calendar
cal = calendar.month(2020, 1)
print ("calender month :",cal)

#time.clock
import time
t = time.localtime()
print("local time :",f"time.asctime(t): {time.asctime(t)}")

# Python program to explain time.gmtime() method

# importing time module
import time

# If secs parameter is not given then the current time as returned by time.time() method is used


# time.struct_time object in UTC. the point where the time starts and return value of time
obj = time.gmtime()
print(obj)

et = ctime()
print(et)

lt = localtime()
print(lt)
print(lt.tm_year)

# month
a = datetime(year = 2022, month = 3, day = 31)
print(a)

dt = datetime(year = 2021, month = 5, day = 20, hour = 15, minute = 35)
print(dt)

dt = datetime(2022,1,31)
print(dt)

dt = (2016, 5, 31, 15, 35)
print(dt)

print(datetime.now())
print(datetime.today())
print(datetime.today().hour)
td = timedelta(days = 10)
d = date.today()
print("Today date: {}, Next date:{}".format(d, d+td))
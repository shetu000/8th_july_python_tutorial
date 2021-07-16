from datetime import date,time,datetime, timedelta

print(date(year=2020,month=10,day=15))
print(time(hour=6,second=31,minute=56)) #here order doesnot matters
print(datetime(year=2020,month=10,day=15 , hour=6,second=31,minute=56))

print(date.today())
print(datetime.now())



#program
from datetime import date,time,datetime
now=datetime.now()
current_time =time(now.hour,now.minute,now.second)
print(datetime.combine(date.today(),current_time)) #it requires parameter. combining today with current_times



#program
from datetime import date,time,datetime
print(date.fromisoformat('2021-07-08'))
d1='01-31-2021 13:21:33'
fmt='%m-%d-%Y %H:%M:%S'
print(datetime.strftime(d1,fmt))

#program
import dateparser
print(dateparser.parse('yesterday'))

#working with timezones
from dateutil import tz
now=datetime.now(tz=tz.tzlocal())
print(now)

#program
from dateutil import tz
print(now.tzname())
print(tz.tzlocal())

#program
from dateutil import tz
london_tz= tz.gettz("Europe/paris")
print(london_tz)
gb_time=datetime.now(tz=london_tz)
print(gb_time)


now=datetime.now()
tommorow= timedelta(days=+1)
print(now)
print(tommorow)
print(now+tommorow)
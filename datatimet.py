from datetime import datetime,timedelta,timezone
import re
dt_str='2015-1-21 9:01:30'
tz_str='UTC+5:00'
ntime=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
com=ntime.timestamp()
th=tz_str[4]
th=int(th)
out=ntime.astimezone(timezone(timedelta(hours=th)))
out=out.timestamp()
print(com)
print(out)
from machine import RTC
import time, ntptime

#rtc.datetime():
#(year, month, day, ?, hour, minute, second, microsecond)

def main(pin, onoff = '1'):
    if (onoff == '1'):
        counter = 0
        start_time = time.localtime()
        print("Start time:", start_time)
        while True:
            if time_diff(time.localtime(), start_time) > 1800: #stop after half an hour
                break
            t0 = time.ticks_ms()
            pin.off() #on
            counter += 1
            print(counter)
            while (time.ticks_diff(time.ticks_ms(), t0) < 100):
                pass
            pin.on() #off
            while (time.ticks_diff(time.ticks_ms(), t0) < 999):
                pass

#d1, d0: (year, month, day)
#returns difference in days
def date_diff(d1, d0):
    daysinyear=lambda y: 365 if (y%4!=0 or (y%100==0 and y%400!=0)) else 366
    daysinmonth=lambda y, m: 31 if m in (1,3,5,7,8,10,12) else 30 if m in (4,6,9,11) else 28 if (y%4!=0 or (y%100==0 and y%400!=0)) else 29
    d1ged0 = True
    if d1[0]<d0[0] or (d1[0]==d0[0] and d1[1]<d0[1]) or (d1[0]==d0[0] and d1[1]==d0[1] and d1[2]<d0[2]):
        d1ged0 = False
    if d1[0] == d0[0]:     #same yr
        if d1[1] == d0[1]: #same mth
            res = d1[2] - d0[2]
            return res if d1ged0 else -res
        res = 0
        for i in range(d0[1], d1[1]): #d0.mth - d1.mth-1
            res += daysinmonth(i)
        res += (d1[2] - d0[2])
        return res if d1ged0 else -res
    res = 0
    for i in range(d0[0], d1[0]): #d0.yr - d1.yr-1
        res += daysinyear(i)
    for i in range(d0[1], d1[1]): #d0.mth - d1.mth-1
        res += daysinmonth(i)
    res += (d1[2] - d0[2])
    return res if d1ged0 else -res

#takes two time tuples returned by time.localtime()
#returns timedelta in seconds
def time_diff(t1, t0):
    timedelta = date_diff(t1[:3], t0[:3]) * 86400
    timedelta += (t1[3] - t0[3]) * 3600
    timedelta += (t1[4] - t0[4]) * 60
    timedelta += (t1[5] - t0[5])
    return timedelta

print(time_diff(time.localtime(), time.localtime()))
# https://docs.python.org/3/library/time.html#time.strftime

import time
# time.asctime() this will give current day,month,date,hour,minute,second,and year.
a=time.strftime("%c,%Z") #has same meaning as asctime()
b=int(time.strftime("%H"))
if(b>=5 and b<12):
    print("Good Morning Sir!")
elif(b>=12 and b<15):
    print("Good Afternoon Sir!")
elif(b>=15 and b<=20):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
print("Current time is:\t",a)
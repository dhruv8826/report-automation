import datetime as t
from dateutil import parser
dateLimit=t.date.today()-t.timedelta(days=7)
i='12/05/2018 15:22:03'
dt=parser.parse(i)
dt=dt.date()
if dt >= dateLimit:
    print (dt,dateLimit)
else:
    print ('No')



#Counting last time system change for n-lastNDays
def lastTimeSystemChange():
    dateLimit=todayDate-t.timedelta(days=lastNDays)
    co=0
    for i in file['Last time status changed']:
        dt=parser.parse(i)
        dt=dt.date()
        if dt >= dateLimit:
            co =co + 1
    return (co)

# 2. Last Time System Change
print("Count of Last time status change for n -",lastNDays,"days are--> ",lastTimeSystemChange())
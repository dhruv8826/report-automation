# importing files
import pandas as pd
import datetime as t
from dateutil.parser import *

# Today's date
todayDate = t.date.today()

# Inputing CSV file
print("Enter the csv file name")
csvFile = input()

# Taking all required inputs
# For last time status change
print("Enter the number of- Last n days")
lastNDays = int(input())

# For total n (on the basis of Pattern date)
print("Enter the number of- Total n(Pattern Date)")
totalN = int(input())

# For server count
print("Enter the number of- Server n")
serverN = int(input())

# For workstation count
print("Enter the number of- Workstation n")
workstationN = int(input())

# Loading CSV as a dataset using pandas
file = pd.read_csv(csvFile, usecols=['Pattern Date','Computer Name','Last time status changed','Operating System'])
# print(file) #for testing

# Counting unique computer names
def uniqueComputerNames():
    file.drop_duplicates(subset='Computer Name',keep='first',inplace=True)
    return len(file['Computer Name'])

# maxTime for last time status changed
maxDate=todayDate-t.timedelta(days=365)
for i in file['Last time status changed']:
    if pd.isnull(i) == False:
        dt = parse(i)
        dt = dt.date()
        if dt >= maxDate:
            maxDate=dt
# assigning maxDate value to todayDate for next part
todayDate = maxDate


# Counting last time system change for n-lastNDays
def lastTimeSystemChange():
    dateLimit = todayDate-t.timedelta(days=lastNDays)
    co1 = 0
    for i in file['Last time status changed']:
        if pd.isnull(i) == False:
            dt = parse(i)
            dt = dt.date()
            if dt >= dateLimit:
                co1 = co1+1
    return co1

# maxTime for patternDate
maxDate=todayDate-t.timedelta(days=365)
for i in file['Pattern Date']:
    if pd.isnull(i) == False:
        dt = parse(i)
        dt = dt.date()
        if dt >= maxDate:
            maxDate=dt
# assigning maxDate value to todayDate for next part
todayDate = maxDate

# Count of pattern date for n-totalN
def patternDateCount():
    dateLimit = todayDate-t.timedelta(days=totalN)
    co2 = 0
    for i in file['Pattern Date']:
        if pd.isnull(i) == False:
            dt = parse(i)
            dt = dt.date()
            if dt >= dateLimit:
                co2 = co2+1
    return co2

# Server count and pattern date
def serverCountAndPattern():
    file['Operating System'] = map(lambda x: x.upper(), file['Operating System'])
    fileServer = file[(['*.SERVER.*','*.CENTOS.*','*.LINUX.*']).isin(file['Operating System'])]
    serverCount = len(fileServer['Operating System'])
    dateLimit = todayDate-t.timedelta(days=serverN)
    co3 = 0
    for i in fileServer['Pattern Date']:
        if pd.isnull(i) == False:
            dt = parse(i)
            dt = dt.date()
            if dt >= dateLimit:
                co3 = co3+1
    serverPatternDateCount = co3
    return serverCount, serverPatternDateCount

# Workstation count and pattern date
def workstationCountAndPattern():
    file['Operating System'] = map(lambda x: x.upper(), file['Operating System'])
    fileWorkstation = file[(['*.SERVER.*','*.CENTOS.*','*.LINUX.*']).notin(file['Operating System'])]
    workstationCount = len(fileWorkstation['Operating System'])
    dateLimit = todayDate-t.timedelta(days=workstationN)
    co4 = 0
    for i in fileWorkstation['Pattern Date']:
        if pd.isnull(i) == False:
            dt = parse(i)
            dt = dt.date()
            if dt >= dateLimit:
                co4 = co4+1
    workstationPatternDateCount = co4
    return workstationCount, workstationPatternDateCount

# Running functions
# 1. Unique Computer Names Count
print("Number of unique Computer Names are--> ", uniqueComputerNames())
# 2. Last Time System Change Count
print("Count of Last time status change for n -", lastNDays, "days are--> ", lastTimeSystemChange())
# 3. Pattern Date Count
print("Count of Pattern Date for n -", totalN, "days is--> ", patternDateCount())
# 4(a). Server Count and Server Pattern Count
serverCount, serverPatternDateCount = serverCountAndPattern()
print("Number of Servers are-->", serverCount)
print("Number of Servers for n - ", serverN, "days is--> ", serverPatternDateCount)
# 4(b). Workstation Count and Server Pattern Count
workstationCount, workstationPatternDateCount = workstationCountAndPattern()
print("Number of Servers are-->", workstationCount)
print("Number of Servers for n - ", serverN, "days is--> ", workstationPatternDateCount)

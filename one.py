#importing files
import pandas as pd
import datetime as t
from dateutil import parser

#Today's date
todayDate=t.date.today()

#Inputing CSV file
print ("Enter the csv file name")
csvFile=input()

#Taking all required inputs
#For last time status change
print("Enter the number of- Last n days")
lastNDays=int(input())

#For total n (on the basis of Pattern date)
print("Enter the number of- Total n")
totalN=int(input())

#For server count
print("Enter the number of- Server n")
serverN=int(input())

#For workstation count
print("Enter the number of- Workstation n")
workstationN=int(input())

#Loading CSV as a dataset using pandas
file=pd.read_csv(csvFile, usecols=['Pattern Date','Computer Name','Last time status changed','Operating System'])
#print(file) #for testing

#Counting unique computer names
def uniqueComputerNames():
    file.drop_duplicates(subset='Computer Name',keep='first',inplace=True)
    return (len(file['Computer Name']))

#Counting last time system change for n-lastNDays
def lastTimeSystemChange():
    dateLimit=todayDate-t.timedelta(days=lastNDays)
    co=0
    for i in file['Last time status changed']:
        if i is not 'nan':
            dt=parser.parse(i)
            dt=dt.date()
            if dt >= dateLimit:
                co=co+1
    return (co)

#Running functions
# 1. Unique Computer Names
print("Number of unique Computer Names are--> ",uniqueComputerNames())
# 2. Last Time System Change
print("Count of Last time status change for n -",lastNDays,"days are--> ",lastTimeSystemChange())
#!/usr/bin/env python
# Python enumeration 
from datetime import datetime

personalInfo =	{
  "dob": "",
  "first name": "",
  "middle name": "",
  "last name": ""
}

for key, value in personalInfo.iteritems():
    print(key.title() + ": " + value)

def getAge():
    current_time = datetime.now()
    date = current_time.strftime('%m/%d/%Y')
    dob = personalInfo["dob"]
    d1 = datetime.strptime(dob, '%m/%d/%Y')
    d2 = datetime.strptime(date, '%m/%d/%Y')
    days = abs((d2 - d1).days)
    years = days / 365
    print("You are " + str(years) + " years old.")
getAge()

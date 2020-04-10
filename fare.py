#fare.py
"""Consists methods and entities to work upon fare(s) for parking lot."""

#FUNCTIONS
def setFare():
    """Shows the current fare saved(None at first),
    and asks the user to change it.""" 
    global fare
    print "CURRENT FARE: Rs.",fare,"per hour"
    try:
        fare = input("What is the new fare?(in INR)\n")
    except SyntaxError:
        print "Enter some value!!\n"
        setFare()
    except NameError:
        print "Enter fare in numbers!!\n"
        setFare()

def calcFare(inTime, outTime):
    """Calculate fare on time for which the vehicle has been parked.
    Use a 24-hour time formats for operation on time calculation.""" 
    fmt = '%H:%M'
    intrvl = str(datetime.strptime(outTime,fmt) - datetime.strptime(inTime,fmt))
    intrvl = intrvl[::-1][3:8][::-1]
    intrvl = intrvl.split(':')
    amt = int(intrvl[0])*fare + int(intrvl[1])/60.0*fare
    return amt

def getTime():
    """Returns a string object of current timestamp in format(24-hour) HH:MM"""
    k = str(datetime.time(datetime.now()))
    k = k[:5]
    return k

#MAIN
from datetime import datetime
fare = None

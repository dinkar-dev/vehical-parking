import pickle
from os import system
from sys import exit as shut
from vehicle import *
from fare import *

def postScr(c=1):
    raw_input("\nPress any key to continue\n")
    if c:
        system('cls')

def menu():
    print """
    +----------------------------------------+
    +-----------------INDEX------------------+
    +----------------------------------------+
    +                                        +
    +   1. VEHICLE ENTRY                     +
    +   2. VEHICLE EXIT                      +
    +   3. SEARCH A PARKED VEHICLE           +
    +   4. SET FARE                          +
    +   5. QUIT APPLICATION                  +
    +                                        +
    +----------------------------------------+
    +----SELECT ANY OPTION FROM ABOVE MENU---+
    +----------------------------------------+
    +---(Invalid option will restart menu)---+
    +----------------------------------------+
    """

    try:
        opt = input(">>>")
    except (SyntaxError, NameError):
        system('cls')
        menu()
    else:
        postScr()
        if opt==1 :
            entry()
            postScr()
            menu()
        elif opt==2 :
            if len(entries) is 0:
                print "Lot is empty!"
            else:
                exit()
            postScr()
            menu()
        elif opt==3:
            if len(entries) is 0:
                print "Lot is empty!"
            else:
                z = search(raw_input("Enter license plate no. of vehicle\n"))
                if z is not None:
                    print z
                else:
                    print "Vehicle not found!"
            postScr()
            menu()
        elif opt==4:
            setFare()
            postScr()
            menu()
        elif opt==5:
            postScr()
            shut()
        else:
            print "WRONG OPTION"
            postScr()
            menu()

def search(seID):
    for x in entries:
        if x.idnum == seID :
            return x  
    return None

def entry():
    print "ENTER OWNER'S DETAILS:-"
    n = mandfield(raw_input("{:12}:{:4}".format("NAME"," ")))
    
    s = mandfield(raw_input("{:12}:{:4}".format("SEX(M/F/NB)",  " ")))
    while s not in ['m','M','f','F','nb','NB'] :
        s = invalid(s)
    
    a = mandfield(raw_input("{:12}:{:4}".format("AGE"," ")))
    while not a.isdigit() :
        a = invalid(a)

    p = mandfield(raw_input("{:12}:{:4}".format("PHONE"," ")))
    while len(p)!=10 or not p.isdigit() :
        p = invalid(p)
    
    print "\nENTER VEHICLE DETAILS:-"
    b = mandfield(raw_input("{:12}:{:4}".format("BRAND"," ")))
    m = mandfield(raw_input("{:12}:{:4}".format("MODEL"," ")))
    c = mandfield(raw_input("{:12}:{:4}".format("COLOR"," ")))
    
    i = mandfield(raw_input("{:12}:{:4}".format("PLATE NUMBER"," ")))
    while len(i)!=4 or not i.isdigit() :
        i = invalid(i)
    
    e = getTime()
    entries.append(vehicle(i,b,m,c,e,n,s,a,p))
    pickle.dump(entries[-1],f1)
    f1.seek(0)
    print "\n{:=^40}\n".format("VEHICLE ENTERED")

def exit():
    exID = search(raw_input("Enter license plate no. vehicle\n"))
    if exID is not None:
        it = exID.entryTime
        ot = getTime()
        exID.exitTime = ot
        print "Vehicle entered at %s and is exiting at %s" % (it,ot)
        print "Collect Rs%.2f from owner!" % calcFare(it,ot)
        postScr(0)
        pickle.dump(exID,f2)
        f2.seek(0)
        entries.remove(exID)
        print "\n{:=^40}\n".format("VEHICLE EXITED")
    else:
        print "Vehicle not found!"

def mandfield(x):
    if x.isspace() or len(x)==0 :
        print "\nField cannot be empty!"
        y = mandfield(raw_input("Enter again:"))
    return x

def invalid(attr):
    print "\nInvalid!"
    attr = mandfield(raw_input("Enter again:"))
    return attr

#------------------------------------MAIN----------------------------------
f = open('logo.txt')
f.seek(0)
for x in range(12):
    print f.readline()
f.close()
postScr()

f1 = open('entry.bin','wb')
f1.seek(0)
f2 = open('exit.bin','wb')
f2.seek(0)
entries = []
setFare()
postScr()
menu()

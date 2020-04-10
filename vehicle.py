class owner(object):

    def __init__(self, name, sex, age, phone):
        self.name = name
        self.sex = sex
        self.age = age
        self.phone = phone

    def __str__(self):
        string = ("OWNER>>""Name:"+str(self.name)+","+"Sex:"+str(self.sex))
        string += (","+"Age:"+str(self.age)+","+"Phone:"+str(self.phone))
        return string

class vehicle(owner):
    
    def __init__(self, idnum, brand, model, color, entryTime, name, sex, age, phone):
        self.idnum = idnum
        self.color = color
        self.brand = brand
        self.model = model
        self.entryTime = entryTime
        self.exitTime = None
        owner.__init__(self, name, sex, age, phone)

    def __str__(self):
        string = ("VEHICLE>>"+"Idnum:"+str(self.idnum)+","+"Color:"+str(self.color))
        string += (","+"Brand:"+str(self.brand)+","+"Model:"+str(self.model))
        string += (","+"EntryTime:"+str(self.entryTime)+","+"ExitTime:"+str(self.exitTime))
        print super(vehicle,self).__str__()
        return string

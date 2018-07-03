import random
class Paitent():
    idNum = 0
    name = ''
    allergies = []
    bedNumber = 0
    def __init__(self, idNum, name, allergies):
        self.idNum = idNum
        self.name = name
        self.allergies = allergies
    #display is used for testing
    def display(self):
        print self.idNum, self.name, self.allergies, self.bedNumber

class Hospital():
    paitents = []
    name = ""
    capacity = 0
    def __init__(self, paitents, name, capacity):
        self.paitents = paitents
        self.name = name
        self.capacity = capacity
    def admit(self, paitent):
        if len(self.paitents) + 1 > self.capacity:
            return "The hospital is full."
        else:
            paitent.bedNumber = random.randint(1,12)
            self.paitents.append(paitent)
            print paitent.bedNumber
            return "Addmission complete."
    def discharge(self, idNum):
        for paitent in self.paitents:
            if paitent.idNum == idNum:
                paitent.bedNumber = 0
                self.paitents.remove(paitent)
        return self
        #used for testing
    def display(self):
        print self.paitents
        print self.name, self.capacity
        return self

pat1 = Paitent(100,"Frank Drebben",["crime", "commitment"])
pat2 = Paitent(101,"some Guy", ["Air"])
hospital = Hospital([pat1],"Our Sister of The Worthless Merical", 1)
#hospital.display()
print hospital.admit(pat2)
pat2.display()
hospital.discharge(101)
pat2.display()

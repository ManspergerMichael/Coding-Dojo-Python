class Car(object):
    def __init__(self):
        self.price = input("What is the price?")
        self.speed = input("How fast is it?")
        self.fuel = input("How much fuel is left?")
        self.mileage = input("How many miles is on it?")
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self. tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: "+str(self.price)
        print "Speed: "+str(self.speed)
        print "Fuel: "+str(self.fuel)
        print "Mileage: "+str(self.mileage)
        print "Tax: "+str(self.tax)
#End of class
   
car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()
car5 = Car()
car6 = Car()
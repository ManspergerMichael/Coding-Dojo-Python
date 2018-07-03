class bike(object):
    price = 0
    max_speed = 0
    miles = 0
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
    def displayInfo(self):
        print "The price is: {}, the maximum speed is: {}, and the total miles: {}.".format(self.price,self.max_speed,self.miles)
        return self
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        self.miles -= 10
        print "Reverseing"
        return self

bike1 =bike(300,30)
bike2 =bike(400, 25)
bike3 =bike(200, 9000)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().displayInfo()





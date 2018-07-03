class Product(object):
    def __init__(self):
        self.price = input("Price?:")
        self.itemName = raw_input("Name?:")
        self.weight = input("Weight?:")
        self.brand = raw_input("Brand?:")
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self,tax):
        return self.price + (self.price * tax)
    def Return(self,reason):
        if(reason == "defective"):
            self.status = reason
            self.price = 0
        if(reason == "in box"):
            self.status = "for sale"
        if(reason == "opened"):
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        return self
    def displayInfo(self):
        print self.price
        print self.itemName
        print self.weight
        print self.brand
        print self.status
        return self

item1 = Product()
item1.displayInfo()
item1.sell()
item1.displayInfo()
print "With tax: "+str(item1.addTax(0.10))
item1.Return("opened")
item1.displayInfo()


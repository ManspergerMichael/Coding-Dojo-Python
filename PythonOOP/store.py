class Store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        for x in range(len(self.products)):
            if(self.products[x].itemName == product):
                self.products.remove(self.products[x])
        return self
    def inventory(self):
        x = 0
        for x in range(len(self.products)):
            print "Name: "+str(self.products[x].itemName)
            print "Price: "+str(self.products[x].price)
            print "Status: "+str(self.products[x].status)
        return self


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
item2 = Product()
store1 = Store("Mysterious Alley Store", "Not the Devil")
store1.add_product(item1).add_product(item2)
store1.inventory()
store1.remove_product("Love")
store1.inventory()
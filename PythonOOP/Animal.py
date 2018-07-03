class Animal(object):
    name = ""
    health = 0
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print str(self.health)
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name,health=150)
    def pet(self):
        health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name,health=170)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print str(self.health) + " I am a Dragon"
        return self
    


anAnimal = Animal("test", 20)
anAnimal.walk().walk().walk().run().displayHealth()

doge = Dog("Wiggles")
doge.walk().walk().walk().run().run().displayHealth()
drag =Dragon("Rue Paul")
drag.walk().run().fly().displayHealth()
#below method calls produce an error 
#anAnimal.pet()
#anAnimal.fly()
#this method call only prints anAnimal's health
#anAnimal.displayHealth()
#doge.fly()
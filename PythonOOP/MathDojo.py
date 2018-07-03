class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self,*args):
        for arg in args:
            if(isinstance(arg,list) or isinstance(arg,tuple)):
                for x in range(len(arg)):
                    #print arg[x]
                    self.total = self.total + arg[x]
            else:
                #print arg
                self.total = self.total + arg
        return self
    def subtract(self,*args):
        for arg in args:
            if(isinstance(arg,list) or isinstance(arg,tuple)):
                for x in range(len(arg)):
                    #print arg[x]
                    self.total = self.total - arg[x]
            else:        
                self.total = self.total - arg
        return self
    def result(self):
        print str(self.total)
        return self

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1],3).result()
tupleNums = (1,2,3,4,5,6)
md.subtract(tupleNums,5).result()
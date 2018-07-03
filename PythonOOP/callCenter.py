
class Call():
    IDNum = 0
    callerName = ""
    callerPhonNum = 0000
    timeOfCall = ""
    callReason =""
    def __init__(self, IDNum, callerName, callerPhonNum, timeOfCall, callReasonn):
        self.IDNum = IDNum
        self.callerName = callerName
        self.callerPhonNum = callerPhonNum
        self.timeOfCall = timeOfCall
        self.callReason =callReasonn
    def displayCallInfo():
        print IDNum, callerName, callerPhonNum, timeOfCall, callReason

class CallCenter():
    calls = []
    queueSize = 0
    def __init__(self, calls):
        self.calls = calls
        self.queueSize = len(calls)
    def add(self, call):
        self.calls.append(call)
        self.queueSize +=1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queueSize -=1
        return self

    def drop(self, number):
        for call in self.calls:
            if call.callerPhonNum == number:
                self.calls.remove(call)
        return self

    def info(self):
        for call in self.calls:
            print "Caller name: {} Caller Number: {}".format(call.callerName, call.callerPhonNum)
        print "There are {} calls in the queue.".format(self.queueSize)
        return self

Buzz = Call(1,"Buzz LightYear", 1234567890, "Noonish", "Delusions")
Woody = Call(2,"Woody", 98765454321, "Evening", "Insecurity")
otherGuy = Call(3, "Some Guy", 1092837465, "Earlyer","N/A")
center = CallCenter([Buzz, Woody])
center.info().add(otherGuy).drop(1092837465).info()

    
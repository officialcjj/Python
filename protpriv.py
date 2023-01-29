class Prot:
    def __init__(self):
        self._protA = 0

obj = Prot()
obj._protA = 1
print(obj._protA)

class Priv:
    def __init__(self):
        self.__protA = 2

    def getPriv(self):
        print(self.__protA)

    def setPriv(self, private):
        self.__protA = private


obj = Priv()
obj.getPriv()
obj.setPriv(3)
obj.getPriv()


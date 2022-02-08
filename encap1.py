class Patient:
    def __init__(self):
        self.name = 'John Doe'
        self._coPay = '50$'

    def setPrivate(self, private):
        self.__diagnosis = private

    def getPrivate(self):
        print(self.__diagnosis)


obj = Patient()
print(obj.name)
obj._coPay = '$25'
print(obj._coPay)
obj.setPrivate('Torn ACL')
obj.getPrivate()

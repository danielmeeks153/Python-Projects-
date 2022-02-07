class Counter:
    def __init__(self):
        self.__current = 0  

    def increment(self):
        self__current += 1

    def value(self):
        return self._current

    def reset(self):
        self.__current = 0 
        
counter = Counter()
print(counter._Counter__current) #accessing the __current attribute  

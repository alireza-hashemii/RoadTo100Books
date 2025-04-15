# when an array is sorted, it makes whole operation of searching easier. since Binary Search can be used.

# bad array
class BadArray:
    def __init__(self, initialsize):
        self.__a = [None] * initialsize
        self.Nitems = 0  
    
    def insert(self, item):
        self.__a.append(item)
        self.Nitems += 1 
    
    def search(self, item) -> str | None:
        for i in range(self.Nitems):
            if self.__a[i] == item:
                return 'Item Found'
        return None
    
    def delete(self, item):
        for i in range(self.Nitems): 
            if self.__a[i] == item:
                self.__a.pop(i)
                return 'Item Deleted'
    
    def traverse(self, function=print): 
        for j in range(self.Nitems): 
            function(self.__a[j])




# a better version
class Array:
    def __init__(self, initialsize):
        self.__a = [None] * initialsize
        self.__nitems = 0

    def get_(self, n):
        if 0 <= n and n <= self.__nitems:
            return self.__a[n]
    
    def set_(self, n, value):
        if 0 <= n and n <= self.__nitems:
            self.__a[n] = value
    
    def insert(self, value):
        self.__a[self.__nitems] = value
        self.__nitems += 1
    
    def find(self, value):
        for i in range(self.__nitems):
            if self.__a[i] == value:
                return 'Item Found'
        
    def delete(self, value):
        for i in range(self.__nitems):
            if self.__a[i] == value:
                self.__a.pop(i)
                self.__nitems =- 1


# Linear Search algorithm is used to search in unordered list.
def sequential_search(numbers:list, value:int):
    for i in numbers:
        if i == value:
            return f'it is found in position {numbers.index(i) + 1}'




# Binary Search will fiind the target at maximum of 7 guesses.
def binary_search(sequence: list, value: int):
    lo = 0
    hi = len(sequence) - 1
    mid = hi // 2
    guess = 0
    while lo <= hi:
        guess += 1
        if sequence[mid] == value:
            return f'Found - {guess}'
        elif sequence[mid] < value:
            lo = mid + 1
            mid = (lo + hi) // 2
        elif sequence[mid] > value:
            hi = mid - 1
            mid = (lo + hi) // 2
    return 'Not Found' 




# simple OrderedArray class - operations are omitted for sake of clarity
class OrderedArray:
    def __init__(self, initialsize:int) -> None:
        self.__a = [None] * initialsize
        self.nitems = 0


    def __len__(self) -> int:
        return self.nitems
    
    def get_(self,  position:int):
        # why position < self.nitems? think about it
        if position > 0 and position < self.nitems:
            return self.__a[position]


    def set_(self, position:int, value):
        if position > 0 and position < self.nitems:
            self.__a[position] = value
            return self.__a[position]


    def __str__(self):
        output = '['
        for i in range(self.nitems):
            output += f',{self.__a[i]}' 
        output += ']'
        return output

        
class Stack:
    def __init__(self, max_size):
        self.__stack = [None] * max_size
        self.__top = -1
    
    def push(self, item):
        self.__top += 1
        self.__stack[self.__top] = item

    def peek(self):
        if not self.isEmpty(): 
            return self.__stackList[self.__top] 

    def pop(self):
        top = self.__stackList[self.__top] 
        self.__stackList[self.__top] = None 
        self.__top -= 1 
        return top

    def __str__(self):
        ans = "[" # Start with left bracket
        for i in range(self.__top + 1): # Loop through current items
            if len(ans) > 1: # Except next to left bracket,
                ans += ", " # separate items with comma
                ans += str(self.__stack[i]) # Add string form of item
                ans += "]" # Close with right bracket
        return ans

    def Isfull(self) -> bool:
        return self.__top >= len(self.__stack) - 1

    def isempty(self) -> bool:
        return self.__top < 0
    
    def __len__(self):
        return self.__top + 1
    



class Queue:
    def __init__(self, size):
        self.__maxsize = size
        self.__rear = 0
        self.__front = 1
        self.__que = [None] * size
        self.__nitems = 0

    def insert(self, item):
        if self.isfull():
            raise Exception('The queue is already reached its maximum size')
        self.__rear += 1 
        if self.__rear == self.__maxsize:
            self.__rear = 0
        self.__que[self.__rear] = item
        self.__nitems += 1
        return True
    
    def remove(self):
        if self.isempty():
            raise Exception("Not possible to remove an item from an empty queue")
        
        front = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front += 1 
        if self.__front == self.__maxsize:
            self.__front = 0
        self.__nitems -= 1
        return front
    
    def peek(self):
        return None if self.isempty() else self.__que[self.__front]

    def isempty(self):
        return len(self.__que) == 0
    
    def isfull(self):
        return len(self.__que) == self.__maxsize
    
    def __len__(self): 
        return self.__nItems
     
    def __str__(self): # Convert queue to string
        ans = "[" # Start with left bracket
        for i in range(self.__nitems): # Loop through current items
            if len(ans) > 1: # Except next to left bracket,
                    ans += ", " # separate items with comma
            j = i + self.__front # Offset from front
            if j >= self.__maxSize: # Wrap around circular array
                j -= self.__maxSize
            ans += str(self.__que[j]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans
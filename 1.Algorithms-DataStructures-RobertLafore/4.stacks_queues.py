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
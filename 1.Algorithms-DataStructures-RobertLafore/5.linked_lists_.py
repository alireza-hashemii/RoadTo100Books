class Link:
    def __init__(self, datum, next_= None):
        self.__data = datum
        self.__next = next_
    
    def get_data(self):
        return self.__data
    
    def set_data(self, datum):
        self.__data = datum

    def get_next(self):
        return self.__next
    
    def set_next(self, new_link):
        if new_link is None or isinstance(new_link, Link):
            self.__next = new_link
        else:
            raise Exception('Next Link Must Be Link or None')
    
    def __str__(self): 
        return str(self.getData())
    


class LinkedList:
    def __init__(self):
        self.__first = None
    
    def getFirst(self): 
        return self.__first

    def setFirst(self, link): # Change the first link to a new Link
        if link is None or isinstance(link, Link): # It must be None or
            self.__first = link # a Link object
        else:
            raise Exception("First link must be Link or None")

    def getNext(self): 
        return self.getFirst()
    
    def setNext(self, link): 
        self.setFirst(link)
    
    def isEmpty(self): 
        return self.getFirst() is None
    
    def first(self):
        if self.isEmpty(): 
            raise Exception('No first item in empty list')
        return self.getFirst().getData() 

    def traverse(self, func = print): 
        l = 0
        link = self.getFirst() # Start with first link
        while link is not None: # Keep going until no more links
            l += 1 # Count Link in chain
            func(link.get_data())
            link = link.get_next() # Move on to next link
            

    def __len__(self):
        l = 0
        link = self.getFirst() 
        while link is not None: 
            l += 1 
            link = link.getNext() 
        return l
    
    
    def insert(self):
        pass

    def __str__(self): 
        result = "[" 
        link = self.getFirst() 
        while link is not None: 
            if len(result) > 1: 
                result += " > " 
            result += str(link)
            link = link.getNext() 
        return result + "]" 



l_1 = Link('salam')
l_2 = Link('chetori', l_1)
l_3 = Link('khobam', l_2)


linked_list = LinkedList()
linked_list.setFirst(l_3)

print(linked_list.traverse())
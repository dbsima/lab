class LinkedList: 
    def __init__(self): 
        self.head = None
        self.length = 0
        
    def is_empty(self):
        return self.length == 0
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.length += 1
        
    def size(self):
        return self.length
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        
    def print_forward(self):
        print "[",
        if self.head != None: 
            self.head.print_forward() 
        print "]",
        
    def print_backward(self): 
        print "[", 
        if self.head != None: 
            self.head.print_backward() 
        print "]",
    
    def add_first(self, cargo): 
        node = Node(cargo) 
        node.next = self.head 
        self.head = node 
        self.length = self.length + 1 

class Node: 
    def __init__(self, cargo=None, next=None): 
        self.cargo = cargo 
        self.next  = next
        
    def get_data(self):
        return self.cargo
    
    def get_next(self):
        return self.next

    def set_data(self, new_cargo):
        self.cargo = new_cargo

    def set_next(self, new_next):
        self.next = new_next
        
    def print_backward(self): 
        if self.next != None: 
            tail = self.next 
        tail.print_backward() 
        print self.cargo,
    
    def print_forward(self):
        while self: 
            print self.cargo, 
            self = self.next 
        
ll = LinkedList()
ll.print_forward()
ll.add(12)
ll.print_forward()
ll.add(12)
print ll.size()
print ll.search(12)
print ll.search(13)

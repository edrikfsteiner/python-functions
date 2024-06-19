class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def get_node(self):
        print(self.value)

class doubly_linked_list:
    def __init__(self):
        self.first = None
        self.last = None
    
    def insert_start(self, value):
        new = node(value)
        
        if self.first is None:
            self.last = new
        else:
            self.first.prev = new

        new.next = self.first
        self.first = new
    
    def insert_end(self, value):
        new = node(value)

        if self.first is None:
            self.first = new
        else:
            self.last.next = new
            new.prev = self.last

        self.last = new
    
    def delete_start(self):
        temp = self.first

        if self.first is not None:
            if self.first.next is None:
                self.last = None
            else:
                self.first.next.prev = None

            self.first = self.first.next
        
        return temp
    
    def delete_end(self):
        temp = self.last

        if self.last is not None:
            if self.last.prev is None:
                self.first = None
            else:
                self.last.prev.next = None

            self.last = self.last.prev
        
        return temp
    
    def delete_any(self, value):
        cur = self.first

        while cur.value != value:
            if cur.next is None:
                return None
            else:
                prev = cur
                cur = cur.next

        if cur == self.first:
            self.first = self.first.next
        else:
            prev.next = cur.next

        return cur

    def display_start(self):
        cur = self.first

        while cur is not None:
            cur.get_node()
            cur = cur.next
    
    def display_end(self):
        cur = self.last

        while cur is not None:
            cur.get_node()
            cur = cur.prev

    def search(self, value):
        cur = self.first

        while cur.value != value:
            if cur.next == None:
                return None
            else:
                cur = cur.next

        return cur

# Uncomment the code below to run the functions
'''
list = doubly_linked_list()

for i in range(3, 0, -1):
    list.insert_start(i)

for j in range(4, 7):
    list.insert_end(j)

list.display_start()
list.delete_start()
list.delete_end()
list.display_end()
list.delete_any(3)
print(list.search(3))
'''
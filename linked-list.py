class node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_node(self):
        print(self.value)

class linked_list:
    def __init__(self):
        self.first = None
    
    def insert(self, value):
        new = node(value)
        new.next = self.first
        self.first = new
    
    def delete(self):
        temp = self.first
        self.first = self.first.next
        return temp
    
    def delete_any(self, value):
        cur = self.first
        prev = self.first

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

    def display(self):
        cur = self.first

        while cur is not None:
            cur.get_node()
            cur = cur.next
    
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
list = linked_list()

for i in range(1, 6):
    list.insert(i)

list.delete_any(3)
list.display()
list.delete()
list.display()
print(list.search(2))
'''
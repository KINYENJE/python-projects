class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        print(f'appended {new_node}')
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count=1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count+1 == position:
                new_element.next =current.next
                current.next = new_element
                return
            else:
                count+=1
                current = current.next
            # break

        pass


        
e1 = Node(1)
print(type(e1))
e2 = Node(2)

l1 = LinkedList(e1) 
l1.append(e2)
print(l1) # <__main__.LinkedList object at 0x00000214D3F6F510>


# a = 2

# def square():
#     global a
#     a = a**2
#     print(a)
# square()
# print(a)

# def increase():
#     global a
#     a+=1
#     print(a)
# increase()
# print(a)


# implementing a stack with a singly linked list


class LinkedStack:
    # Nested _Node class
    class _Node:
        """" lightweight nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's field
            self._element = element  # reference to user’s element
            self._next = next  # reference to next node

    # ------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """return number of elements in a stack"""
        return self._size

    def is_empty(self):
        """Return true if stack is empty"""
        return self._size == 0

    def push(self, e):
        """add element e to top of stack"""
        self._head = self._Node(e, self._head)  #create and link a new node
        self._size += 1

    def top(self):
        """Return element at top of the stack"""
        if self.is_empty():
            raise ReferenceError ('Stack is empty')
        return self._head._element  # top of the stack is aat head of list

    def pop(self):
        """Remove and return element from the top of the stack"""

        """Raise empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def print_stack(stack):
    currentNode = stack._head  # start at the top of the stack
    while currentNode is not None:
        print(currentNode._element)
        currentNode = currentNode._next


stack = LinkedStack()
stack.push(10)
stack.push(20)
stack.push("yoww")
stack.push(30)

print("Element popped is ",  stack.pop())

stack_size = len(stack)
print("Size of the stack:", stack_size)

print("Stack elements are:")
print_stack(stack)


print("Stack elements at top:", stack.top())

while not stack.is_empty():
    popped_element = stack.pop()
    print("Popped element:", popped_element)
print("Is the stack empty?", stack.is_empty())
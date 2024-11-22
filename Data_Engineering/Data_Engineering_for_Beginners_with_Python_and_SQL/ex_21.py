class Stack:
    def __init__(self):
        # Initialize an empty list to use as the stack
        self.stack = []

    def push(self, item):
        # Push the item onto the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        # Return the item at the top of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.stack) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

assert stack.pop() == 3  # Should print 3
assert stack.peek() == 2  # Should print 2
assert stack.is_empty() == False  # Should print False
assert stack.size() == 2  # Should print 2

# Example of a test that will fail
def test_fail_pop_on_empty_stack():
    stack = Stack()
    try:
        stack.pop()
    except IndexError as e:
        print("Test failed as expected with IndexError:", str(e))

def test_fail_peek_on_empty_stack():
    stack = Stack()
    try:
        stack.peek()
    except IndexError as e:
        print("Test failed as expected with IndexError:", str(e))

# Example usage:
test_fail_pop_on_empty_stack()
test_fail_peek_on_empty_stack()

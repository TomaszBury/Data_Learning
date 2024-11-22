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
            return "Stack is empty"

    def peek(self):
        # Return the item at the top of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

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

print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.is_empty())  # Should print False
print(stack.size())  # Should print 2
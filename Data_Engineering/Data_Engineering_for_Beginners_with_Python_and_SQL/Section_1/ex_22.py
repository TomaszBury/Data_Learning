class Queue:
    def __init__(self):
        # Initialize an empty list to use as the queue
        self.queue = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

# Example usage:
queue = Queue()
assert queue.peek() == 0  # Should print 0
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

assert queue.dequeue() == 1  # Should print 1
assert queue.peek() == 2  # Should print 2
assert queue.is_empty() == False  # Should print False
assert queue.size() == 2  # Should print 2

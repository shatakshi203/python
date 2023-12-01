class StackAndQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack_queue = StackAndQueue()
stack_queue.push(1)
stack_queue.push(2)
stack_queue.enqueue(3)
stack_queue.enqueue(4)

print("Stack and Queue:", stack_queue.items)
print("Pop:", stack_queue.pop())
print("Dequeue:", stack_queue.dequeue())
print("Size:", stack_queue.size())


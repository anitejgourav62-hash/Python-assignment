from collections import deque
class Queue:
    def _init_(self):
        self.queue = deque()

    # Method to add element
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    # Safe dequeue method
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            removed = self.queue.popleft()
            print(removed, "removed from queue")
            return removed

    # Display queue
    def display(self):
        print("Queue:", list(self.queue))
q = Queue()

q.safe_dequeue()   
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.safe_dequeue()
q.display()
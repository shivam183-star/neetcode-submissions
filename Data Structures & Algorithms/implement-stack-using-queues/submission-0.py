from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def isempty(self):
        if self.queue:
            return False
        return True

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.isempty():
            return None
        return self.queue.popleft()
    
    def front(self):
        if self.isempty():
            return None
        return self.queue[0]
    
    def length(self):
        return len(self.queue)

class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        for _ in range(self.queue.length() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        if self.queue.isempty():
            return None
        return self.queue.dequeue()

    def top(self) -> int:
        return self.queue.front()

    def empty(self) -> bool:
        if self.queue.isempty():
            return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
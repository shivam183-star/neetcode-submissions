from collections import defaultdict


class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}

    def length(self):
        return len(self.map)

    def insert(self, val):
        if val not in self.map:
            node = Node(val)
            self.map[val] = node

            last = self.tail.prev

            last.next = node
            node.prev = last

            node.next = self.tail
            self.tail.prev = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]

            prev = node.prev
            nxt = node.next

            prev.next = nxt
            nxt.prev = prev

            del self.map[val]

    def remove(self):
        if self.length() == 0:
            return None

        lru = self.head.next.val
        self.pop(lru)

        return lru


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.frequencyMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)

        self.capacity = capacity
        self.least = 0

    def counter(self, key):
        freq = self.frequencyMap[key]

        self.listMap[freq].pop(key)

        self.frequencyMap[key] += 1

        self.listMap[freq + 1].insert(key)

        if freq == self.least and self.listMap[freq].length() == 0:
            self.least += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.counter(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.counter(key)
            return

        if len(self.cache) == self.capacity:
            lfu = self.listMap[self.least].remove()

            del self.cache[lfu]
            del self.frequencyMap[lfu]

        self.cache[key] = value

        self.frequencyMap[key] = 1

        self.listMap[1].insert(key)

        self.least = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
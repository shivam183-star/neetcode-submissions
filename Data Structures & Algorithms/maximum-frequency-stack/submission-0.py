class FreqStack:

    def __init__(self):
        self.freq = {}
        self.groups = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        self.groups[f].append(val)
        self.maxFreq = max(self.maxFreq, f)

    def pop(self) -> int:
        x = self.groups[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
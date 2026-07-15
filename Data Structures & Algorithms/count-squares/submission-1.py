class CountSquares:

    def __init__(self):
        self.freq = {}

    def add(self, point: list[int]) -> None:
        if tuple(point) not in self.freq:
            self.freq[tuple(point)] = 0
        self.freq[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        c1 , c2 = 0, 0
        x, y = point[0], point[1]
        for px, py in self.freq.keys():
            if px == x and y != py:
                d = abs(y - py)
                if (x+d, y) in self.freq and (x+d, py) in self.freq:
                    c1 += self.freq[(x+d, y)] * self.freq[(x+d, py)] * self.freq[(x, py)]
                if (x-d, y) in self.freq and (x-d, py) in self.freq:
                    c2 += self.freq[(x-d, y)] * self.freq[(x-d, py)] * self.freq[(x, py)]
        return c1 + c2
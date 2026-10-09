class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]

        self.count -= 1


class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        uf = UnionFind(len(nums))

        factors = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factors:
                        uf.union(i, factors[f])
                    else:
                        factors[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factors:
                    uf.union(i, factors[n])
                else:
                    factors[n] = i

        return uf.count == 1
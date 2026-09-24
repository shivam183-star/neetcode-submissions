class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v):
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key= lambda x: x[2])

        mst = 0
        uf = UnionFind(n)
        for u, v, w, i in edges:
            if uf.union(u, v):
                mst += w

        critic, pseudo = [], []
        for u1, v1, w1, index in edges:
            weight = 0
            uf = UnionFind(n)

            for u, v, w, i in edges:
                if index == i:
                    continue
                if uf.union(u, v):
                    weight += w

            if max(uf.rank) != n or weight > mst:
                critic.append(index)
                continue

            weight = w1
            uf = UnionFind(n)
            uf.union(u1, v1)
            for u, v, w, i in edges:
                if uf.union(u, v):
                    weight += w

            if weight == mst:
                pseudo.append(index)

        return [critic, pseudo]

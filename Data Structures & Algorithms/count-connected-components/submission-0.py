class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        components = n
        def find(x):
            if parent[x] != x:
               parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
               return False
            else:
                parent[rootB] = rootA
                return True
        
        for u, v in edges:
            if union(u , v):
                components -= 1
        
        return components
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return True
            else:
                parent[rootB] = rootA
                return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
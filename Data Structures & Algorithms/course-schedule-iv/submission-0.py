class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        
        def dfs(i, j):
           for nei in graph[j]:
               if not isReachable[i][nei]:
                   isReachable[i][nei] = True
                   dfs(i, nei)
        
        for i in range(numCourses):
            dfs(i, i)
        
        res = []
        for u, v in queries:
            res.append(isReachable[u][v])
        
        return res
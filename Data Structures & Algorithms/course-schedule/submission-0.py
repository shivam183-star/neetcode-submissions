class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)

        states = [0] * numCourses
        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            
            states[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = 2
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
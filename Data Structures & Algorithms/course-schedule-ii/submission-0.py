class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        visiting = set()
        order = []
        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            order.append(node)
            visiting.remove(node)
            visited.add(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return order
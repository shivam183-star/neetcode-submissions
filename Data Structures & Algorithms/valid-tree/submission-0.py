class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False
        
        if dfs(0, -1):
            return False
        return len(visited) == n
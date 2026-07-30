class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            u = equations[i][0]
            v = equations[i][1]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        def dfs(a, b, res, visited):
            visited.add(a)
            if a == b:
                return res
            for nei, w in graph[a]:
                if nei not in visited:
                    ans = dfs(nei, b, res * w, visited)
                    if ans != -1:
                        return ans
            return -1
        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1)
            else:
                res = dfs(a, b, 1, set())
                result.append(res)
        
        return result
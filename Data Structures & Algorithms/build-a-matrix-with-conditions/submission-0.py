class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(node, order, visited, path, graph):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            visited.add(node)

            for nei in graph[node]:
                if not dfs(nei, order, visited, path, graph):
                    return False
            order.append(node)
            path.remove(node)
            return True

        def topoSort(condition):
            graph = defaultdict(list)
            for u, v in condition:
                graph[u].append(v)
            order, visited, path = [], set(), set()
            for node in range(1, k + 1):
                if not dfs(node, order, visited, path, graph):
                    return []

            return order[::-1]

            


        row_order = topoSort(rowConditions)
        col_order = topoSort(colConditions)
        if not row_order or not col_order:
            return []
        row_idx = {n : i for i, n in enumerate(row_order)}
        col_idx = {n : i for i, n in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]

        for num in range(1, k+1):
            r, c = row_idx[num], col_idx[num]
            res[r][c] = num

        return res

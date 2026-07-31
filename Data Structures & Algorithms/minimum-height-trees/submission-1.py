class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        degrees = [len(graph[i]) for i in range(n)]

        queue = deque()
        for i in range(n):
            if degrees[i] == 1:
                queue.append(i)
        rem = n
        while rem > 2:
            size = len(queue)
            rem -= size
            for _ in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    degrees[nei] -= 1

                    if degrees[nei] == 1:
                        queue.append(nei)
        
        return list(queue)


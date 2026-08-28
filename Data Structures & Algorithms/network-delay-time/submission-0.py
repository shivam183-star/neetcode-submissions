class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n+1)
        queue = [(0, k)]
        visited = set()
        while queue:
            w, node = heapq.heappop(queue)

            if node in visited:
                continue
            visited.add(node)
            dist[node] = w

            for nei, next in graph[node]:
                if nei not in visited:
                    heapq.heappush(queue, (w + next, nei))

        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1


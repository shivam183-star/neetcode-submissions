class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            curr = points[i]
            for j in range(i+1, len(points)):
                next = points[j]
                graph[tuple(curr)].append((abs(curr[0] - next[0]) + abs(curr[1] - next[1]), tuple(next)))
                graph[tuple(next)].append((abs(curr[0] - next[0]) + abs(curr[1] - next[1]), tuple(curr)))

        visited = set()
        cost = 0
        minHeap = [(0, tuple(points[0]))]

        while len(visited) < len(points):
            w, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            cost += w

            for weight, next in graph[node]:
                if next not in visited:
                    heapq.heappush(minHeap, (weight, next))

        return cost
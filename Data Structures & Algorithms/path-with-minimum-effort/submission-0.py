class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        minHeap = [[0, 0, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nr == rows or nc < 0 or nc == cols) or (nr, nc) in visited:
                    continue

                heapq.heappush(minHeap, [max(diff, abs(heights[nr][nc] - heights[r][c])), nr, nc])
                
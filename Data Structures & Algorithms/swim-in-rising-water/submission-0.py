class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        visited.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]]

        while minHeap:
            e, r, c = heapq.heappop(minHeap)

            if (r, c) == (rows - 1, cols - 1):
                return e

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(minHeap, [max(e, grid[nr][nc]), nr, nc])
        
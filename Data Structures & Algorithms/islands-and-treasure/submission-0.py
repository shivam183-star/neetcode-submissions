class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647
        queue = deque()
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == INF:
                        grid[nr][nc] = min(grid[nr][nc], 1 + grid[r][c])
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
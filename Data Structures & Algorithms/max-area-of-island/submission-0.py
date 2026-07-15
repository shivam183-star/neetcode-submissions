class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        maxarea = 0
        for r in range(rows):
            for c in range(cols):
                maxarea = max(dfs(r, c), maxarea)
        return maxarea
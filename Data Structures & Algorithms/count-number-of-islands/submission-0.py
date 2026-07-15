class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r,c))
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    dfs(r, c)
        return count

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp = {}
        def dfs(r, c):
            
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            dp[(r, c)] = res
            return res
        
        lip = 0
        for r in range(rows):
            for c in range(cols):
                lip = max(dfs(r, c), lip)
        
        return lip
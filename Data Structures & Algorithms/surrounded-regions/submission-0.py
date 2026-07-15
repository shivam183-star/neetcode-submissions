class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            board[r][c] = "T"
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols-1]):
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
               
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
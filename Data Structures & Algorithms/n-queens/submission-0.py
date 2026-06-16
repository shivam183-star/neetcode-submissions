class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos = set()
        neg = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board].copy())
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue

                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos = set()
        neg = set()

        count = 0

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue

                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)

                backtrack(r+1)
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        
        backtrack(0)
        return count
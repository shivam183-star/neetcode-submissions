class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        
        def backtrack(i, j, index):
            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= r or j >= c:
                return False
            
            if board[i][j] != word[index]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"
            found = (backtrack(i-1, j, index + 1) or backtrack(i, j+1, index + 1) or backtrack(i+1, j, index + 1) or backtrack(i, j-1, index + 1))
            board[i][j] = temp
            return found
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False
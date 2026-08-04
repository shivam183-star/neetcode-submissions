class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add(word)

        rows = len(board)
        cols = len(board[0])

        res, visited = set(), set()

        def dfs(r, c, node, word):
            if 0 > r or r >= rows or 0 > c or c >= cols or (r, c) in visited or board[r][c] not in node.children:
                return

            node = node.children[board[r][c]]
            word += board[r][c]
            visited.add((r, c))

            if node.end:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
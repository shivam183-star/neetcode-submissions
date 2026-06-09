class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1

            char = chr((columnNumber % 26) + ord("A"))
            res.append(char)

            columnNumber = columnNumber // 26
        return "".join(res[::-1])
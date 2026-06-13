class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for ch in mapping[digits[i]]:
                backtrack(i+1, curr + ch)

        if digits:
            backtrack(0, "")
        return res
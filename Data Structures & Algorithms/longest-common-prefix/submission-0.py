class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
        
        return res

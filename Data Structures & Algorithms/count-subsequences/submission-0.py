class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, curr):
            if curr == t:
                return 1
            if i == len(s):
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            ways = 0
            ways += (dfs(i + 1, curr + s[i]) + dfs(i+1, curr))
            dp[(i, curr)] = ways
            return ways

        return dfs(0, "")
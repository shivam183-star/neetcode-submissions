class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        dp = {}

        def dfs(i):
            
            if i == len(s):
                return True
            
            if i in dp:
                return dp[i]
            dp[i] = False
            for j in range(i, len(s)):
                if s[i: j+1] in wordDict:
                    if dfs(j+1):
                        dp[i] = True
                        break                
            return dp[i]
        
        return dfs(0)


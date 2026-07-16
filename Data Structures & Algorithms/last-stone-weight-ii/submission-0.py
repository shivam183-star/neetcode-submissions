class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sumstones = sum(stones)
        target = math.ceil(sumstones / 2)

        dp = {}

        def dfs(i, total):
            if target <= total or i == n:
                return abs(total - (sumstones - total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))
            return dp[(i, total)]
        
        return dfs(0, 0)

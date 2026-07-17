class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i , total) in dp:
                return dp[(i, total)]
            count = dfs(i + 1, total + nums[i]) + dfs(i+1, total - nums[i])
            dp[(i, total)] = count
            return count
        
        return dfs(0, 0)
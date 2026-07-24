class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax = 0
        globalmax = nums[0]
        currmin = 0
        globalmin = nums[0]
        total = 0

        for n in nums:
            currmax = max(currmax + n, n)
            globalmax = max(globalmax, currmax)
            currmin = min(currmin + n, n)
            globalmin = min(currmin, globalmin)
            total += n
        if globalmax < 0:
            return globalmax
        return max(globalmax, total - globalmin)

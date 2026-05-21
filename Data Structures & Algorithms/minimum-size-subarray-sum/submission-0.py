class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        i = 0
        min_len = float("inf")
        for j in range(len(nums)):
            window_sum = window_sum + nums[j]
            while window_sum >= target:
                min_len = min(min_len, j - i + 1)
                window_sum = window_sum - nums[i]
                i = i + 1
        if min_len != float("inf"):
            return min_len
        else:
            return 0
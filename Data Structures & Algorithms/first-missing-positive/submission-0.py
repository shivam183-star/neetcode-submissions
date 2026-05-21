class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1
        s = set(nums)
        while n in s:
            n += 1
        return n
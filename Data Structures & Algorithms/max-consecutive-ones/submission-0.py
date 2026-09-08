class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxc = 0
        for num in nums:
            if num == 0:
                c = 0
            else:
                c += 1
            maxc = max(c, maxc)
        return maxc
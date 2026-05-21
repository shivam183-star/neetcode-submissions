class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in comp:
                return [comp[c], i]
            comp[num] = i


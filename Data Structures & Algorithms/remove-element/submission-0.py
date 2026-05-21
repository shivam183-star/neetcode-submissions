class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(0, n):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
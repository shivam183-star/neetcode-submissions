class Solution:
    def check(self, mid, nums, k):
        sum = 0
        i = 1
        for num in nums:
            if sum + num > mid:
                i += 1
                sum = num
            else:
                sum = sum + num
        return i <= k
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            if self.check(mid, nums, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod =1 
        right = [0] * len(nums)
        left = []
        res = []
        for i in range(len(nums)):
            left.append(prod)
            prod = prod * nums[i]
        prod = 1
        for j in range(len(nums)-1, -1, -1):
            right[j] = prod
            prod = prod * nums[j]
        for k in range(len(nums)):
            res.append(left[k] * right[k])

        return res
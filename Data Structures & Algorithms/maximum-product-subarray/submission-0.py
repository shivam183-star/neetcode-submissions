class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for curr in nums[1:]:
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(max_prod * curr, curr)
            min_prod = min(min_prod * curr, curr)
            ans = max(max_prod, ans)
        return ans
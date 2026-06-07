class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, target, subset):
            if target == 0:
                result.append(subset.copy())
                return
            
            if i >= len(nums) or target < 0:
                return

            subset.append(nums[i])

            backtrack(i, target - nums[i], subset)
            subset.pop()
            backtrack(i+1, target, subset)

        backtrack(0, target, [])
        return result

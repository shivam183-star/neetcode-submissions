class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n
        nums.sort()
        def backtrack(subset):
            if len(subset) >= n:
                
                result.append(subset.copy())
                return
            
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and not used[i - 1]:
                    continue
                if used[i]:
                    continue
                subset.append(nums[i])
                used[i] = True
                backtrack(subset)
                subset.pop()
                used[i] = False
            
        backtrack([])
        return result
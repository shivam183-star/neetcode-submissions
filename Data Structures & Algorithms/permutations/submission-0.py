class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n

        def backtrack(subset):
            if len(subset) >= n:
                result.append(subset.copy())
                return
            
            for i in range(n):

                if used[i]:
                    continue
                subset.append(nums[i])
                used[i] = True
                backtrack(subset)
                subset.pop()
                used[i] = False
            
        backtrack([])
        return result


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False
        
        subsum = total // k
        nums.sort(reverse=True)

        def dfs(i, subsets):
            if i == len(nums):
                return True
            
            for j in range(k):
                if nums[i] + subsets[j] > subsum:
                    continue

                subsets[j] += nums[i]
                if dfs(i+1, subsets):
                    return True

                subsets[j] -= nums[i]

                if subsets[j] == 0:
                    break
            return False
        
        return dfs(0, [0]*k)
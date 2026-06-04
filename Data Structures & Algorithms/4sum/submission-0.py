class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            for k in range(l + 1, len(nums)):
                
                if k > l+1 and nums[k] == nums[k-1]:
                    continue

                i = k + 1
                j = len(nums) - 1
                while i < j:
                    sum = nums[l] + nums[k] + nums[i] + nums[j]
                    if sum == target:
                        res.append([nums[l], nums[k], nums[i], nums[j]])
                        i += 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                    
                    elif sum > target:
                        j -= 1
                    else:
                        i += 1
                
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1

            while i < j:
                sum = nums[k] + nums[i] + nums[j]
                if sum == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif sum > 0:
                    j -= 1
                else:
                    i += 1
        return res
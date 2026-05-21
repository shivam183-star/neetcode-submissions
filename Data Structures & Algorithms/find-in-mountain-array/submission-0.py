class Solution:
    def binarysearch(self, nums, low, high, target, asc):
        while low <= high:
            mid = (low + high)//2
            val = nums.get(mid)
            if val == target:
                return mid
            if asc:
                if val < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if val < target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1



    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        nums = mountainArr
        low = 0
        high = nums.length() - 1
        while low < high:
            mid = (low + high)//2
            
            if nums.get(mid) < nums.get(mid + 1):
                low = mid + 1
            else:
                high = mid 
        peak = low

        ans = self.binarysearch(nums, 0, peak, target, True)
        if ans != -1:
            return ans
        
        return self.binarysearch(nums, peak + 1, nums.length() - 1, target, False)


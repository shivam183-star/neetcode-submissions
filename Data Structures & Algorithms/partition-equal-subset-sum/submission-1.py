class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for num in nums:
            next = set()
            for s in dp:
                next.add(num + s)
                next.add(s)
                if num + s == target:
                    return True
            dp = next
        return False
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = [0]
        for num in nums:
            next = []
            for s in dp:
                if num + s not in dp:
                    next.append(num + s)
                if num + s == target:
                    return True
            dp += next
        return False
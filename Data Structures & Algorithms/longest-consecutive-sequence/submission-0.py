class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxc = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                current = num

                while (current + 1) in numSet:
                    current += 1
                    count += 1

                maxc = max(maxc, count)

        return maxc
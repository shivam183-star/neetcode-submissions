class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        ways = 0

        for c in freq.values():
            if c == 1:
                return -1
            if c % 3 == 0:
                ways += c // 3
            else:
                ways += c // 3 + 1

        return ways
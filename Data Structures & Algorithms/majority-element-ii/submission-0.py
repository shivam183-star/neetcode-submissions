class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for i in list(freq.keys()):
            if freq[i] > len(nums)//3:
                res.append(i)
        return res
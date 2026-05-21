class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        ele = [(freq[x], x) for x in freq.keys()]
        ele.sort(reverse= True)
        res = []
        for i in range(k):
            res.append(ele[i][1])
        return res
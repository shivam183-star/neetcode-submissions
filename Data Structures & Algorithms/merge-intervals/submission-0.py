class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key= lambda x : x[0])

        prev = [intervals[0][0], intervals[0][1]]
        for start, end in intervals[1:]:
            if start <= prev[1]:
                prev = [prev[0], max(prev[1], end)]
            else:
                res.append(prev)
                prev = [start, end]
        res.append(prev)
        return res
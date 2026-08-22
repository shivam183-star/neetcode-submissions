class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []

        for i, ch in enumerate(s):
            if ch not in last:
                last[ch] = i
            last[ch] = i
        end = 0
        size = 0
        for i in range(len(s)):
            size += 1
            end = max(end, last[s[i]])

            if i == end:
                res.append(size)
                size = 0

        return res
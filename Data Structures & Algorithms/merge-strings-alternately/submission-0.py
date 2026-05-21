class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        l1 = len(word1)
        l2 = len(word2)
        while i < l1 and j < l2:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        while i < l1:
            res.append(word1[i])
            i += 1
        while j < l2:
            res.append(word2[j])
            j += 1
        return "".join(res)

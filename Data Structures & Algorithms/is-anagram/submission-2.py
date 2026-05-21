class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for i in t:
            freq[i] = freq.get(i, 0) + 1
        for char in s:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0

        for j in range(len(s)):
            if s[j] == t[i]:
                i += 1
            if i == len(t):
                return 0
        
        return len(t) - i 
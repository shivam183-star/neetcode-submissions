class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seen = set()
        maxlen = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxlen = max(maxlen, j - i + 1)
        return maxlen


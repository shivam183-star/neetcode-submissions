class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        maxfreq = 0
        maxlen = 0
        freq = {}
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxfreq = max(maxfreq, freq[s[j]])

            while (j - i + 1) - maxfreq > k:
                freq[s[i]] -= 1
                i += 1
            maxlen = max(maxlen , j - i + 1)
        return maxlen
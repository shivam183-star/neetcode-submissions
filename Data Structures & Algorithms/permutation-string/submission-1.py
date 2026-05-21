class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1
        l = len(s1)
        window = s2[:l]
        freq2 = {}
        for ch in window:
            freq2[ch] = freq2.get(ch, 0) + 1
        if freq1 == freq2:
                return True
        for i in range(l, len(s2)):
            freq2[s2[i-l]] -= 1
            if freq2[s2[i-l]] == 0:
                del freq2[s2[i-l]]
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
            if freq1 == freq2:
                return True
        return False 
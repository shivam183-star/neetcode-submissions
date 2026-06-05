class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        freqt = Counter(t)
        freqs = {}
        i = 0
        res = [-1, -1]
        reslen = float('inf')
        have, need = 0, len(freqt)
        for j in range(len(s)):
            c = s[j]
            freqs[c] = freqs.get(c, 0) + 1
            
            if c in freqt and freqs[c] == freqt[c]:
                have += 1
            
            while have == need:
                if (j - i + 1) < reslen:
                    res = [i, j]
                    reslen = j - i + 1

                freqs[s[i]] -= 1
                if s[i] in freqt and freqs[s[i]] < freqt[s[i]]:
                    have -= 1
                i += 1
        
        if reslen != float('inf'):
            return s[res[0] : res[1] + 1]
        else:
            return ""

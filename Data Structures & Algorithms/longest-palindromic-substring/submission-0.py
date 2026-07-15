class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        reslen = 0
        def expand(i, j):
            nonlocal res, reslen
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        return res
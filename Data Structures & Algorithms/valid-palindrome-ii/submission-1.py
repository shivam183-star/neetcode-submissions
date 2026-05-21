class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[right] != s[left]:
                return isPal(left +1, right) or isPal(left, right - 1)
            left += 1
            right -= 1
        return True


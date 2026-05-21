class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c for c in s if c.isalnum()).lower()
        return result == result[::-1]
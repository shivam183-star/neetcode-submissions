class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 + str2 == str2 + str1:
            return ""
        
        l1 = len(str1)
        l2 = len(str2)

        for i in range(min(l2, l1), 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                gcd = i
                break
        
        return str1[:gcd]

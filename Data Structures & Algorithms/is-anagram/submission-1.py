class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst = [i for i in t]
        for i in s:
            if i not in lst:
                return False
            lst.remove(i)
        return True
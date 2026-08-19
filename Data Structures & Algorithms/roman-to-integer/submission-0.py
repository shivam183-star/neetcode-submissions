class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        for i in range(len(s) - 1):
            curr = values[s[i]]
            if curr < values[s[i+1]]:
                num -= curr
            else:
                num += curr
        
        num += values[s[-1]]
        return num
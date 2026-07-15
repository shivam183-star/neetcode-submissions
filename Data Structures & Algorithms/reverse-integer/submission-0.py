class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 214748364
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        ans = 0
        while x:
            digit = x % 10
            if ans > INT_MAX or (ans == INT_MAX and digit > 7):
                return 0
            
            ans = ans * 10 + digit
            x = x // 10
            
        return sign * ans
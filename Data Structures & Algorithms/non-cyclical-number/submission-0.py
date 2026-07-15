class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            sum = 0
            while n:
                d = n % 10
                sum += d**2
                n = n // 10
            
            if sum == 1:
                return True
            if sum in seen:
                return False

            seen.add(sum)
            n = sum    
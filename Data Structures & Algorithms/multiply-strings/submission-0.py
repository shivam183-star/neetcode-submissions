class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        res = [0] * (n + m)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                n1 = int(num1[i])
                n2 = int(num2[j])
                p2 = i + j + 1
                p1 = p2 - 1

                prod = n1 * n2
                sum = prod + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10
        
        i = 0
        while i < len(res) and res[i] == 0 :
            i += 1
        return "".join(map(str, res[i:])) if res[i:] else "0"


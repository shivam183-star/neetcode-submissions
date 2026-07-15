class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    rem = i - c
                    num = 1 + dp[rem]
                    dp[i] = min(num, dp[i])
        print(dp)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount] 
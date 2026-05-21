class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        start = prices[0]
        for i in range(1, len(prices)):
            if start < prices[i]:
                maxprofit = maxprofit + prices[i] - start
            start = prices[i]
        return maxprofit
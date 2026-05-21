class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        profit = 0
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i]< minprice:
                minprice = prices[i]
            profit = prices[i] - minprice
            maxprofit = max(maxprofit, profit)

        return maxprofit
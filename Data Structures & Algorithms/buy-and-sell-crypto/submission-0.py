class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i,p in enumerate(prices):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit 
                # profit = max(profit, max_profit)
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]

        for r in range(len(prices)):
            if min_price > prices[r]:
                min_price = prices[r]
            else:
                profit = prices[r] - min_price 
                max_profit = max(max_profit,profit)
        
        return max_profit

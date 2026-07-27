class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices: 
            return 0 
        

        l = 0 
        max_profit = 0 
        for r in range(1, len(prices)): 
            buy = prices[l]

            if prices[r] > prices[l]: 
                sell = prices[r] - prices[l]
                max_profit = max(sell , max_profit)
            else: 
                l = r 
        
        return max_profit
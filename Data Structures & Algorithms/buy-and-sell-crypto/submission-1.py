class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            input - list of prices i is the price of neetCoin on the ith day 
            output - is the max profit after selling the coin 
        '''
        max_profit = 0
        min_price = prices[0]

        for r in range(len(prices)):
            if min_price > prices[r]:
                min_price = prices[r]
            else: 
                profit = prices[r] - min_price
                max_profit = max(profit, max_profit)
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            input - list of prices i is the price of neetCoin on the ith day 
            output - is the max profit after selling the coin 
        '''
        max_profit = float("-inf")
        
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        
        return max_profit 
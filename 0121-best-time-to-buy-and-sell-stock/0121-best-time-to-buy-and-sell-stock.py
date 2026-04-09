class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        if len(prices) == 1:
            return max_profit
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price:
                max_profit  =  max(max_profit, prices[i]-min_price)    
        return max_profit        
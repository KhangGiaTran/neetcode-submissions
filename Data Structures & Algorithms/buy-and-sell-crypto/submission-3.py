class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for i, price in enumerate(prices):
            if i == 0: 
                continue
            max_profit = max(max_profit, price - prices[l])

            if price < prices[l]:
                l = i
        return max_profit
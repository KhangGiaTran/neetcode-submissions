class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for i, price in enumerate(prices):
            if i == 0: continue
            if price < prices[l]:
                l = i
            else:
                max_profit = max((price - prices[l]), max_profit)

        return max_profit
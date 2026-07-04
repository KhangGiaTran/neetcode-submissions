class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for i, price in enumerate(prices):
            max_profit = max(price - prices[l], max_profit)

            if price <= prices[l]:
                l = i

        return max_profit
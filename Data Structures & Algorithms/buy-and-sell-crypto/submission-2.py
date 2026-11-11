class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minprices = prices[0]
        maxprices = 0

        for price in prices:
            profit = price - minprices
            if profit > maxprices:
                maxprices = profit
            if price < minprices:
                minprices = price
        return maxprices

        
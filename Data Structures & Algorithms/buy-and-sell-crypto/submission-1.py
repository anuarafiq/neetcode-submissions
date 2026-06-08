class Solution:
    def maxProfit(self, prices: List[int]):
        n = len(prices)
        max_profit = 0

        curr_min = float('inf')
        for i in range(1, n):
            curr_min = min(prices[i-1], curr_min)
            profit = prices[i] - curr_min
            max_profit = max(max_profit, profit)

        return max_profit
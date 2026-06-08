class Solution:
    def maxProfit(self, prices: List[int]):
        n = len(prices)
        min_left = [float('inf')] * n
        max_profit = 0

        curr_min = float('inf')
        for i in range(1, n):
            curr_min = min(prices[i-1], curr_min)
            min_left[i] = curr_min
            profit = prices[i] - min_left[i]
            max_profit = max(max_profit, profit)

        return max_profit
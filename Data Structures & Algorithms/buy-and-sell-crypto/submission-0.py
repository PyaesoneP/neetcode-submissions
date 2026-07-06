class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0

        while r < len(prices):
            can_grow = prices[r] >= prices[l]
            if can_grow:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
            else:
                l = r
        return max_profit

                



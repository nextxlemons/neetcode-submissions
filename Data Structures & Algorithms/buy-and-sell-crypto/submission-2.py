class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                curr_profit = prices[j] - prices[i]
                if profit < curr_profit:
                    profit = curr_profit
                j += 1
            else:
                i = j
                j += 1
        return profit

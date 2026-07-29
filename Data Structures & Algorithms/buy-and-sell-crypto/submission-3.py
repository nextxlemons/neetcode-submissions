class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                res = prices[j] - prices[i]
                profit = max(res, profit)
            else:
                i = j

        return profit

        

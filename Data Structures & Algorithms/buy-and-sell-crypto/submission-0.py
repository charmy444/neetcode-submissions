class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxes = [0 for i in range(len(prices))]
        mins = [0 for i in range(len(prices))]
        m1 = 101
        m2 = -1
        res = 0
        for i in range(len(prices)):
            if prices[i] < m1:
                m1 = prices[i]
            mins[i] = m1
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > m2:
                m2 = prices[i]
            maxes[i] = m2
        for i in range(len(prices)):
            if maxes[i] - mins[i] > res:
                res = maxes[i] - mins[i]
        return res
            
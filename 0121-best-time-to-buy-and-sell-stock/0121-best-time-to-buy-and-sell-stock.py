class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lo=0
        hi=1
        profit=0
        while hi<len(prices):
            if prices[lo]<prices[hi]:
                income=prices[hi]-prices[lo]
                profit=max(profit,income)
            else:
                lo=hi
            hi+=1
            
        return profit
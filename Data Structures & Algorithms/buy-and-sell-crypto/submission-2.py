class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 #buy
        r = 1 #sell
        
        profit = 0

        while r < n:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
            
 #[10,1,5,6,7,1]           
 # pl = 1, pr= 7, profit = 6, l=1, r = 4

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(x):
            cnt = 0
            for p in piles:
                cnt += math.ceil(p / x)
            return cnt <= h
        
        # F, F, F, (T), T, T, T
        l, r = 0, max(piles)
        while l + 1 < r:
            mid = (r + l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid
        return r
        
            
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k=1 -> sum = list.sum() -> h < Sum?
        # k = max(piles)

        l = 1
        r = max(piles)

        k_min = r

        while l <= r:
            mid = (l + r) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(p/mid)
            if total_time <= h:
                k_min = mid
                r = mid - 1
            else:
                l = mid + 1
        return k_min



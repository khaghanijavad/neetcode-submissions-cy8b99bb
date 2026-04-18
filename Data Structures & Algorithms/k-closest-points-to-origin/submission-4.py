import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(i):
            x, y = points[i]
            return x * x + y * y

        def partition(l, r):
            # 1) pick random pivot and move it to the end
            pivot_idx = random.randint(l, r)
            points[pivot_idx], points[r] = points[r], points[pivot_idx]

            pivot_dist = dist(r)
            i = l

            # 2) standard partition
            for j in range(l, r):
                if dist(j) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            # 3) place pivot in correct position
            points[i], points[r] = points[r], points[i]
            return i

        l, r = 0, len(points) - 1

        while l <= r:
            pivot = partition(l, r)

            if pivot == k:
                break
            elif pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1

        return points[:k]
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        heap = []
        for num, cnt in hm.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for cnt, num in heap]


        


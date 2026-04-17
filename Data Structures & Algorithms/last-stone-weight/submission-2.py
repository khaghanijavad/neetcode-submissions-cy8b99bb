class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python -> Min Heap 
        # -s -> Max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        


        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)
        
        if not len(stones):
            return 0
        else:    
            return abs(stones[0])


        
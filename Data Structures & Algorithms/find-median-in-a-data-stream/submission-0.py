import heapq

class MedianFinder:

    def __init__(self):
        # lower half (as negatives)
        self.maxHeap = []  

        # upper half
        self.minHeap = []  

    def addNum(self, num: int) -> None:
        # Step 1: push to maxHeap (as negative)
        heapq.heappush(self.maxHeap, -num)

        # Step 2: move largest of lower half to upper half
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Step 3: balance sizes (minHeap can have at most 1 extra)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
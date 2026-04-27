import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  # lower half as negatives
        self.minHeap = []  # upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (self.minHeap[0] - self.maxHeap[0]) / 2
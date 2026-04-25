class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphMap = {i: [] for i in range(n+1)}
        for u, v, t in times:
            # (node, time)
            graphMap[u].append((v, t))
        
        # (time, node)
        meanHeap = [(0, k)]

        visit = set()
        time = 0

        while meanHeap:
            w1, n1 = heapq.heappop(meanHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time, w1)
            for n2, w2 in graphMap[n1]:
                if n2 not in visit:
                    heapq.heappush(meanHeap, (w2+w1, n2))
        return time if len(visit) == n else -1
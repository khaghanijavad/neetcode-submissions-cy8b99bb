import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for _ in range(n + 1)]
        hm = {}
        for num in nums: 
            hm[num] = 1 + hm.get(num, 0)
        
        for num, cnt in hm.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(n, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
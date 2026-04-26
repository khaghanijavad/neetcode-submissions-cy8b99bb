class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        
        for c in tasks:
            freq[ord(c) - ord('A')] += 1
        
        maxFreq = max(freq)
        maxCount = freq.count(maxFreq)
        
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)
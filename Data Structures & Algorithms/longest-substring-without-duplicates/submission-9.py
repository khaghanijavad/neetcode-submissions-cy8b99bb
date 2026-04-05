class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # keep latest index of a char
        l = 0
        largest = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            largest = max(largest, r - l + 1)
        return largest
            
        

        
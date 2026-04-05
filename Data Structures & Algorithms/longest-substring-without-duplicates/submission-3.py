class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        l = 0
        seen = set(s[l])
        largest = 1
        counter = 1
        r = 1
        while r < len(s): 
            if s[r] not in seen:
                counter += 1
                seen.add(s[r])
                r += 1
                largest = max(largest, counter)
            else:
                l += 1
                r = l + 1
                counter=1
                seen = set(s[l])
        return largest  


        
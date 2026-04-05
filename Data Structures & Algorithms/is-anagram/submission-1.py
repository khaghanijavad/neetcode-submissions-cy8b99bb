class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        if len(s) != len(t):
            return False
        
        for c in s: 
            if c not in hm:
                hm[c] = 1
            else: 
                hm[c] += 1

        for c in t:
            if c not in hm:
                return False
            else: 
                hm[c] -=1
            if hm[c] < 0:
                return False

        return True
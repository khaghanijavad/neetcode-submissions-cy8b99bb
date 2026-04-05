class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        if len(s) != len(t):
            return False
        
        for c1 in s: 
            if c1 not in hm1:
                hm1[c1] = 1
            else: 
                hm1[c1] +=1

        for c2 in t: 
            if c2 not in hm2:
                hm2[c2] = 1
            else: 
                hm2[c2] +=1

        for c in hm1:
            if (c not in hm2):
                return False
            else:
                if hm1[c] != hm2[c]:
                    return False
        return True
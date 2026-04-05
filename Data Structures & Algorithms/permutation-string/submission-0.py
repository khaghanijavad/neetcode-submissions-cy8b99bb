class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = [0] * 26
        s2w_chars = [0] * 26

        n_s1 = len(s1)
        n_s2 = len(s2)

        if len(s1)>len(s2):
            return False
        
        for c in s1:
            s1_chars[ord(c) - ord("a")] += 1
        
        l = 0
        for r in range(n_s2):
            s2w_chars[ord(s2[r]) - ord("a")] += 1
            
            # shrink window if larger than len(s1)
            if r - l + 1 > n_s1:
                s2w_chars[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if s2w_chars == s1_chars:
                return True

        return False
            
        
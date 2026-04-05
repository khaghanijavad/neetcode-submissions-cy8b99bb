class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        characters = [0] * 26
        length = 0

        l=0
        maxf = 0 
        
        n = len(s)
        for r in range(n):
            r_ascii = ord(s[r]) - ord("A")    
            characters[r_ascii] += 1
            maxf = max(maxf, characters[r_ascii])

            while (r - l + 1) - maxf > k:
                l_ascii = ord(s[l]) - ord("A")   
                characters[l_ascii] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length

            
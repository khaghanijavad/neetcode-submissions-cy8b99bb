class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        #characters = [0] * 26
        length = 0
        unique_s = set(s)
        for c in unique_s: 
            l=0
            counter = 0
            for r in range(n):
                if c == s[r]:
                    counter +=1
                while (r - l + 1) - counter > k:
                    if s[l] == c:
                        counter -=1
                    l += 1
                length = max(length, r - l + 1)
        return length

            
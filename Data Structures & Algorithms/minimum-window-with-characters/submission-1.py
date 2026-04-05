class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t = {}
        count_sub_s = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        l = 0
        existing_keys = 0 
        required_keys = len(count_t)
        best = float("infinity")
        res = [-1, -1]
        
        for r in range(len(s)):
            count_sub_s[s[r]] = count_sub_s.get(s[r], 0) + 1
            
            # See if window matches ref count for current char
            freq_s_r = count_sub_s[s[r]]
            freq_t_r = count_t.get(s[r], 0)
            if freq_s_r == freq_t_r:
                existing_keys += 1

            # prune to shortest
            while existing_keys == required_keys:
                width = r - l + 1
                if width < best:
                    best = r - l + 1
                    res = [l, r]
                    
                count_sub_s[s[l]] -= 1
                freq_s_l = count_sub_s[s[l]]
                freq_t_l = count_t.get(s[l], 0)
                if freq_s_l < freq_t_l:
                     existing_keys -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if best != float("infinity") else ""

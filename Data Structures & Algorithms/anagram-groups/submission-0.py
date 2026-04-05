class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for idx, word in enumerate(strs):
            counts = [0] * 26
            for c in word: 
                counts[ord(c) - ord('a')] += 1
            
            key = tuple(counts)
            if key in table:
                table[key].append(word)
            else: 
                table[key] = [word]
                
        return list(table.values())
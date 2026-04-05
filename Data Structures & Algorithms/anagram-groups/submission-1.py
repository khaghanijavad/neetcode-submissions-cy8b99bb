class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for idx, word in enumerate(strs):
            counts = [0] * 26
            for c in word: 
                counts[ord(c) - ord('a')] += 1
            
            key = tuple(counts)
            if key not in table:
                table[key] = []
            table[key].append(word)
        return list(table.values())
# Tuple can be index of dict, but list can't
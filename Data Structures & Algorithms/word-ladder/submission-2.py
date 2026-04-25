class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternMap = {}
        nChar = len(endWord)
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        for w in wordList:
            for i in range(nChar):
                pattern = w[:i] + "*" + w[i+1:]
                if pattern not in patternMap:
                    patternMap[pattern] = []
                patternMap[pattern].append(w)

        visit = set()
        visit.add(beginWord)
        out = 1
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return out
                for c in range(nChar):
                    p = w[:c] + "*" + w[c+1:]
                    adjs = patternMap[p]
                    for adj in adjs:
                        if adj not in visit:
                            q.append(adj)
                            visit.add(adj)
            out += 1
        return 0




        
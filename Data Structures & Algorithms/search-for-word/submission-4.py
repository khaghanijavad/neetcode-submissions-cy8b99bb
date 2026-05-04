class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if (not ((0 <= r < rows) and (0 <= c < cols))) or ((r, c) in visit) or (board[r][c] != word[i]):
                return False
             
            if i == len(word) - 1:
                return True


            visit.add((r, c))
            out = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visit.remove((r, c))

            return out

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
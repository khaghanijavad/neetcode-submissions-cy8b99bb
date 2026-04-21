class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, visit):
            if not(0<=r<rows and 0<=c<cols) or board[r][c] == "X" or (r, c) in visit:
                return
            board[r][c] = "T"
            visit.add((r, c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

        # Unsurrounded Os to T
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col, visit)
            if board[rows-1][col] == "O":
                dfs(rows-1, col, visit)
         
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0, visit)
            if board[row][cols-1] == "O":
                dfs(row, cols-1, visit)

        # Remaining, aka surrounded Os to X
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visit and board[i][j] == "O":
                    board[i][j] = "X"

        # Ts (Unsurrounded Os) back to O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

        
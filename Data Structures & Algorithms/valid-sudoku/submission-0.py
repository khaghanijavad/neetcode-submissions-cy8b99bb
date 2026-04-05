class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                else:
                    if row not in rows:
                        rows[row] = set()
                    if col not in cols:
                        cols[col] = set()
                    if (row // 3, col //3) not in squares:
                        squares[(row // 3, col //3)] = set()

                    if (board[row][col] in rows[row]) or (board[row][col] in cols[col]) or (board[row][col] in squares[(row // 3, col //3)]):
                        return False
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[(row // 3, col //3)].add(board[row][col])
        return True
                    



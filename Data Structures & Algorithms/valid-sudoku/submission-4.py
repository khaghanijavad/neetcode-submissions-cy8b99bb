class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                else:
                    value = int(value) - 1
                    bit_rep = (1<<value)

                    if (bit_rep & rows[row]) or (bit_rep & cols[col]) or (bit_rep & squares[(row // 3) * 3 + (col // 3)]):
                        return False
                    
                    
                    rows[row] |= bit_rep
                    cols[col] |= bit_rep
                    squares[(row // 3) * 3 + (col // 3)] |= bit_rep
        return True
                    



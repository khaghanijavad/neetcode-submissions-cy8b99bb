# Start from top-right or bottom-left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        row_index = 0 
        col_index = m-1
        while row_index < n and col_index >= 0:
            current = matrix[row_index][col_index] #matrix[n-1][0]
            if current < target:
                row_index += 1
            elif current > target:
                col_index -= 1
            else:
                return True
        return False

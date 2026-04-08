
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n -1


        while l <= r:
            mid = (l + r) // 2
            row_index = mid // n 
            col_index = mid % n
            #print ("####", m, n)
            #print(mid, row_index, col_index)
            val = matrix[row_index][col_index]

            if target > val: 
                l = mid + 1
            elif target < val: 
                r = mid - 1
            else:
                return True
        return False
         
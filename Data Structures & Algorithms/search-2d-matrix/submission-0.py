class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        
        return any([self.binary_search(target, matrix[n], 0) for n in range(n_row)])
    


    def binary_search(self, target, nums, offset):
        if not nums:
            return False

        mid = len(nums) // 2

        if target > nums[mid]:
            return self.binary_search(target, nums[mid + 1:], offset + mid + 1)
        elif target < nums[mid]:
            return self.binary_search(target, nums[:mid], offset)
        else:
            return True
        
        
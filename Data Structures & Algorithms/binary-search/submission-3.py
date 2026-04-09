class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #F, F, F, (T), F, F
        l, r = -1, len(nums)

        while l + 1 < r: 
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                r = mid
            else:
                l = mid
        return -1
                            
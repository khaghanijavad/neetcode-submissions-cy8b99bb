class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        output= -1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]

            diff = target - val
            
            if diff == 0:
                return mid

            #Left side rotated sorted array 
            if val >= nums[l]:
                if target < nums[l] or target > val:
                    l = mid + 1
                else:
                    r = mid - 1

            #Right side rotated sorted array
            else:
                if target < val or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
        return -1
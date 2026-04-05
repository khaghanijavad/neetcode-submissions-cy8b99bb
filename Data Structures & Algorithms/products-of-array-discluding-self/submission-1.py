class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1 for i in range(n)], [1 for i in range(n)]
        #prefix[0] = 1
        #suffix[n-1] = 1 
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[n-1-i] = nums[n-i] * suffix[n-i]
        
        return [x * y for x, y in zip(prefix, suffix)]


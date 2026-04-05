class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n  
        suffix = [1]*n
        result = [1]*n
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[n-1-i] = nums[n-i] * suffix[n-i]
        
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result


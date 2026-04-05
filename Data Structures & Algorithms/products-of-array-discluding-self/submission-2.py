class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, result = [1 for i in range(n)], [1 for i in range(n)], [1 for i in range(n)]
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[n-1-i] = nums[n-i] * suffix[n-i]
        
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result


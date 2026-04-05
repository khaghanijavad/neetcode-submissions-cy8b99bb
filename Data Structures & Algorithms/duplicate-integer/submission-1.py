class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_values = set()
        for i, val in enumerate(nums):
            if val not in seen_values: 
                seen_values.add(val)
            else:
                return True
        else:
            return False
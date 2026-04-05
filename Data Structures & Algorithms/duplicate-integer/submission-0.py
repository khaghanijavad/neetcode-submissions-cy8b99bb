class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_index_dict = {}
        for i, val in enumerate(nums):
            if val not in value_index_dict: 
                value_index_dict[val] = [i]
            else:
                return True
        else:
            return False
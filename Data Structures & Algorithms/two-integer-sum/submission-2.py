class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = []
        for idx, val in enumerate(nums):
            remaining.append(target - val)

        for idx, val in enumerate(remaining): 
            if (val in nums) and (nums.index(val) != idx):
                return sorted([idx, nums.index(val)])

#nums = [3, 4, 5, 6]
#target = 7

#remaining = [4, 3, 2, 1]

        
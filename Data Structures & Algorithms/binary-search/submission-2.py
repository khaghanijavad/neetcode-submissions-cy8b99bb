class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(target, nums, 0)

    def binary_search(self, target, nums, offset):
        if not nums:
            return -1

        mid = len(nums) // 2

        if target > nums[mid]:
            return self.binary_search(target, nums[mid + 1:], offset + mid + 1)
        elif target < nums[mid]:
            return self.binary_search(target, nums[:mid], offset)
        else:
            return offset + mid
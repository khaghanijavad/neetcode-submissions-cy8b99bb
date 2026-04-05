class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # a + b + c = 0
            a = nums[i]
            
            # if a is positive, since it's sorted there is no 3sum==0
            if a>0:
                break

            # skip duplicates for first number
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    #while left < right and nums[right] == nums[right + 1]:
                    #    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
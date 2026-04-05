class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        left = 0
        right = n - 1

        while left != right:
            temp = numbers[left] + numbers[right]
            if temp>target:
                right -=1
            elif temp<target:
                left +=1
            else:
                return [left+1, right+1]
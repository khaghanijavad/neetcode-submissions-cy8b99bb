class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        output = [0] * n

        for i, temp in enumerate(temperatures):
            while len(stack) and temp > temperatures[stack[-1]]:
                output[stack[-1]]= int(i - stack[-1])
                stack.pop()
            stack.append(i)
        return output
            
                    
#[30,38,30,36,35,40, 6: 28]    
# stack [5, 6]
# output [1 4 1 2 1 0 0]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)

        stack = []
        for p, s in pairs:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)

#[4, 1, 0, 7]
#[0, 1, 4, 7]
#[0, 1, 4], p=7, t=3, stack=[3], 
#[0, 1], p=4, t=3, stack=[3]
#[0], p=1, t=4.5, stack=[3, 4.5]
#[], p=0, t=10, stack=[3, 4.5, 10]

#[1, 4]
#[1, 4]
#[1], p=4, t=3, stack=[3]
#[], p=1, t=3, stack=[3]



#1, 4, 7, 10
#4, 6, 8, 10


#4, 6, 7, 8, 9, 10
#1, 3, 5, 7, 9, 11
#0, 1 ,2, 3, 4, 5, 6, 7, 8 ,9, 10
#7, 8, 9, 10

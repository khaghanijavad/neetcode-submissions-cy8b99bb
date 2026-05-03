class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        out = []


        def backtrack(nOpen, nClose):
            if nOpen == nClose == n:
                out.append("".join(stack))
            
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen + 1, nClose)
                stack.pop()
            
            if nClose < nOpen: 
                stack.append(")")
                backtrack(nOpen, nClose + 1)
                stack.pop()
            
        backtrack(0, 0)
        return out

        
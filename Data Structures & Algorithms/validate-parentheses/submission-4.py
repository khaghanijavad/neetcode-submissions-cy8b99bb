class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            #Opening 
            if c in mapping:
                stack.append(c)
            #Closing
            else:
                if stack == [] or mapping[stack.pop()] != c:
                    return False
        return True if not stack else False

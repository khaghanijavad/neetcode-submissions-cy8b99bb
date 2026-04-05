class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        n = len(s)
        for i in range(int(n//2)):
            if s[i]!=s[n-1-i]:
                return False
        return True
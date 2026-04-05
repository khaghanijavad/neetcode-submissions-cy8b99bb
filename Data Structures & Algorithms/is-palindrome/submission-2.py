class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if self.isalnum(c)).lower()
        n = len(s)
        for i in range(int(n//2)):
            left = i
            right = n-1-i
            if s[left] != s[right]:
                return False
        return True

    def isalnum(self, c):
        if ((ord("A")<= ord(c) <= ord("Z")) or (ord("a")<= ord(c) <= ord("z")) or (ord("0")<= ord(c) <= ord("9"))):
            return True
        
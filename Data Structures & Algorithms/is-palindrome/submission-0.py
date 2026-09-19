class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = [x for x in s if x.isalnum()]
        if len(s) % 2 == 0:
            n = len(s) // 2 - 1
        else:
            n = (len(s) + 1) // 2 - 1
        for i in range(n+1):
            if s[i] != s[-1 * i - 1]:
                return False
        return True
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) % 2 == 0:
            n = (len(s) // 2) - 1
        else:
            n = (len(s) + 1) // 2 - 1
        for i in range(n + 1):
            s[i], s[-1 * i - 1] = s[-1 * i - 1], s[i]
        
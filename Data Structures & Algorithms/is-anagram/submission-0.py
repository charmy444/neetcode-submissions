class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = ord("a")
        ht = [0 for _ in range(26)]
        for i in s:
            ht[ord(i) - char] += 1
        for i in t:
            ht[ord(i) - char] -= 1
        return ht == [0 for _ in range(26)]
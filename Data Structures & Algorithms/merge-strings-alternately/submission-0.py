class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        min_list = 1 if len(word1) < len(word2) else 2
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i]
            res += word2[i]
        if min_list == 1:
            return res + word2[min_len:]
        else:
            return res + word1[min_len:]
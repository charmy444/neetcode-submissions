class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p = 0
        p2 = 0
        while p2 < len(abbr):
            if p >= len(word): return False
            if not abbr[p2].isdigit():
                if word[p] == abbr[p2]:
                    p += 1
                    p2 += 1
                else:
                    return False
            else:
                c = ""
                while p2 < len(abbr) and abbr[p2].isdigit():
                    c += abbr[p2]
                    p2 += 1
                if len(c) > 1 and c[0] == "0":
                    return False
                else:
                    p += int(c)
                    if p > len(word):
                        return False
        if p > len(word): return False
        return True
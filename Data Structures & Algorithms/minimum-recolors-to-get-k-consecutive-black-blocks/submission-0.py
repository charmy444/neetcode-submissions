class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 101
        r, l = 0, 0
        curr = 0
        while r < len(blocks):
            if r - l + 1 > k:
                if blocks[l] == "W":
                    curr -= 1
                l += 1
            if blocks[r] == "W":
                curr += 1
            if r - l + 1 == k:
                res = min(res, curr)
            r += 1
        return res
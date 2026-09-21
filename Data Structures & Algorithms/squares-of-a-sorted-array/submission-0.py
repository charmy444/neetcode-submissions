class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = [abs(x) for x in nums[::-1] if x < 0]
        m = [x for x in nums if x >= 0]
        res = []
        p1, p2 = 0, 0
        while p1 < len(n) or p2 < len(m):
            if p1 >= len(n):
                res.append(m[p2]**2)
                p2 += 1
            elif p2 >= len(m):
                res.append(n[p1]**2)
                p1 += 1
            else:
                if n[p1] > m[p2]:
                    res.append(m[p2]**2)
                    p2 += 1
                else:
                    res.append(n[p1]**2)
                    p1 += 1
        return res
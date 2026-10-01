class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = 0
        res = 0
        l, r = 0, 0
        while r < len(arr):
            if r - l + 1 > k:
                curr -= arr[l]
                l += 1
            curr += arr[r]
            if r - l + 1 == k:
                if curr / k >= threshold:
                    res += 1
            r += 1
        return res


        
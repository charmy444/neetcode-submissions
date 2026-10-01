class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 100001
        for i in range(k-1, len(nums)):
            res = min(res, nums[i] - nums[-1 * k + 1 + i])
        return res
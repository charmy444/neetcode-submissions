class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        ht = {}
        while r < len(nums):
            if r - l > k:
                del ht[nums[l]]
                l += 1
            if nums[r] not in ht:
                ht[nums[r]] = r
            else:
                return True
            r += 1   
        return False
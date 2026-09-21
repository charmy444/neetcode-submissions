class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, c = 0, 1
        if len(nums) == 1:
            return 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                c += 1
                nums[l] = nums[r]
        for i in range(len(nums) - c):
            nums.pop()
        return c

            

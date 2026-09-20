class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1, p2 = 0, 0
        n = len(nums)
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        for i in range(n - p1):
            nums.pop()
        for i in range(n - p1):
            nums.append(0)
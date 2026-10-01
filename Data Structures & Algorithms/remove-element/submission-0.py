class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_len = len(nums)
        p = 0
        for i in nums:
            if i != val:
                nums[p] = i
                p += 1
        for i in range(start_len - p):
            nums.pop()
        for i in range(start_len - p):
            nums.append("_")
        return p

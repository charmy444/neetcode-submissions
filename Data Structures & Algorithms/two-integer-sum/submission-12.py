class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, value in enumerate(nums):
            if value not in ht:
                ht[value] = [i]
            else:
                ht[value].append(i)
        for i, value in enumerate(nums):
            if target - value in ht:
                if ht[target - value][0] == i:
                    if len(ht[target - value]) > 1:
                        return [i, ht[target - value][1]]
                    else:
                        continue
                else:
                    return [i, ht[target - value][0]]

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return ls

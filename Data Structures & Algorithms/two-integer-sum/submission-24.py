class Solution:
    def twoSum(self, nums, target):
        numsI = {}

        for i in range(len(nums)):
            numsI[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsI and numsI[diff] != i:
                return [i ,numsI[diff]]

        return []

        






        
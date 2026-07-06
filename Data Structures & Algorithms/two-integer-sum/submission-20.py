class Solution:
    def twoSum(self, nums, target):
        twoSum = []
        twoSumMap = {}

        for i in range(len(nums)):
            twoSumMap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in twoSumMap and i != twoSumMap[diff]:
                return [i,twoSumMap[diff]]

        return []

        






        
class Solution:
    def twoSum(self, nums, target):
        
        sumHash = {}
        for i in range(len(nums)):
            sumHash[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sumHash:
                if sumHash[diff] != i:
                    return [i, sumHash[diff]]

        return []






        
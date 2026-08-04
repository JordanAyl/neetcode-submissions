class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsH = {}

        for i in range(len(nums)):
            numsH[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numsH and numsH[diff] != i:
                return [i, numsH[diff]]

        return []
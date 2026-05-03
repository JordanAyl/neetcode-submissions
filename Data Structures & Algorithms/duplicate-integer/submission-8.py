class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        testNums = nums
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    if nums[x] == testNums[y]:
                        return True
        
        return False



        
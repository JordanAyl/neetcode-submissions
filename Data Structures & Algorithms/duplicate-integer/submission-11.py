class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theSet = set(nums)
        if len(theSet) == len(nums):
            return False
        return True


        
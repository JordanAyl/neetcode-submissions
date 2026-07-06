class Solution:
    def hasDuplicate(self, nums):
        di = set(nums)

        return len(di) != len(nums)

        
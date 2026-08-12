class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums[0] == 1 and len(nums) == 1:
            return 1
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                l = r + 1
            count = max(count, (r - l) + 1)

        return count
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = nums[0]
        for i in nums:
            lowest = min(i, lowest)

        return lowest


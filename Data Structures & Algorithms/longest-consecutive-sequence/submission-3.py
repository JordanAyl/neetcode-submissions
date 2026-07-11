class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        hasht = {}

        if not nums:
            return 0

        for i in range(len(nums)):
            hasht[nums[i]] = i

        for i in nums:
            thislong = 1
            while i + 1 in hasht:
                thislong += 1
                longest = max(longest, thislong)
                i += 1

        return longest




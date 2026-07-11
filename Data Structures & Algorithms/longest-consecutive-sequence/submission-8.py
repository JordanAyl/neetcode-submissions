class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longest = 1
        for num in numSet:

            if num - 1 in numSet:
                length = 1
                while num + length -1 in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

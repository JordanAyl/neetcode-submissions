class Solution:
    #binary search has a pivot and minimizes that amount to search
    #through each time by get rid of of one of the halfs of the list
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid

            else:
                l = mid + 1
        
        return nums[l]


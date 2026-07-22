class Solution:
    #binary search has a pivot and minimizes that amount to search
    #through each time by get rid of of one of the halfs of the list
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # start at beginning
        l, r = 0, len(nums) - 1

        #break if l is greater than r
        while l <= r:
            #compare left and right
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #create mid point
            m = (l + r) // 2
            #comp min of res to mid
            res = min(res, nums[m])
            #if mid is larger than l than make mid+1 the new l
            if nums[m] >= nums[l]:
                l = m + 1
            #if mid is larger than r than make mid+1 the new r
            else:
                r = m - 1
        return res
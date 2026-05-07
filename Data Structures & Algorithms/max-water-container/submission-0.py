class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """ height lowest bar^2 *
         length apart from each other return"""
        """
        Two Pointer because have to find all caluclations in arr
        """

        res = 0
        l , r = 0, len(heights) - 1

        while l < r:
            # calculate area with curent left and right bars
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            #move the pointer with the shorter bar inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res

            
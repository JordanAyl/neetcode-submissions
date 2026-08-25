class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        p = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            p = max(p, h* (r - l))

            if heights[l] < heights[r]:
                l += 1
                continue
            else:
                r -= 1
                continue

        return p
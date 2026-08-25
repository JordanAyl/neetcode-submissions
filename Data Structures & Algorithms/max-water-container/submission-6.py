class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        product = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            product = max(product, height * (r - l))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return product
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        best = 0
        while left < right:
            water = 0
            if heights[left] < heights[right]:
                water = heights[left] * (right - left)
                left += 1
            else:
                water = heights[right] * (right - left)
                right -= 1

            if water >= best:
                best = water
            
        return best
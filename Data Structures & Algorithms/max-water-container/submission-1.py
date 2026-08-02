class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        result = 0
        while l < r:
            if heights[l] > heights[r]:
                result = max(heights[r] * (r - l), result)
                r -= 1
            else:
                result = max(heights[l] * (r - l), result)
                l += 1
        return result
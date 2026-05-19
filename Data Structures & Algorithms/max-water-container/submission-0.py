class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = -1
        while left < right:
            width = min(heights[left], heights[right])
            length = right - left
            res = max(res, width*length)
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return res
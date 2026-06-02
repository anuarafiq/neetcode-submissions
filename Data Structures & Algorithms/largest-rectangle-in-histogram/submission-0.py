class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        area = -1

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                curr_idx = stack.pop()
                width = i - 1 - stack[-1] if stack else i
                curr_area = heights[curr_idx] * width
                area = max(area, curr_area)
            stack.append(i)
        
        while stack:
            curr_idx = stack.pop()
            width = n - 1 - stack[-1] if stack else n
            curr_area = heights[curr_idx] * width
            area = max(area, curr_area)

        return area
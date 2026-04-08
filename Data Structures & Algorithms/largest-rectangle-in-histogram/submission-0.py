class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # each item: (height, width)
        max_area = 0

        while heights:
            height = heights.pop()
            width = 1

            while stack and height <= stack[-1][0]:
                prev_height, prev_width = stack.pop()
                width += prev_width
                max_area = max(max_area, prev_height * (width - 1))

            stack.append((height, width))
            max_area = max(max_area, height * width)

        width = 0
        while stack:
            height, w = stack.pop()
            width += w
            max_area = max(max_area, height * width)

        return max_area

# height=4, width=1, stack=[(4, 1)], max_area=4
# height=2, width=2, stack=[(2, 2)], max_are=4
# height=2, width=3, 
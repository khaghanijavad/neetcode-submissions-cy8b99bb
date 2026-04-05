class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # volume = width  * height
        # width = j - i
        # height = min(heights[i], heights[j])
        n = len(heights)
        l = 0
        r = n -1
        max_vol = 0

        while l < r:
            width = r-l
            height = min(heights[l], heights[r])
            max_vol = max(max_vol, width*height)
            if heights[l]<heights[r]:
                l = l + 1
            else:
                r = r - 1
        
 
        return max_vol


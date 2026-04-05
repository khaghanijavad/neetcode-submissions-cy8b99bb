class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        water = 0
        left_max = height[l]
        right_max = height[r]
        while l<r:
            if height[l] < height[r]:
                l = l + 1
                left_max = max(left_max, height[l])
                water = water + (left_max - height[l])
            else:
                r = r - 1
                right_max = max(right_max, height[r])
                water = water + (right_max - height[r])
        return water


        
        
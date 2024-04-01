class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) -1
        
        while left<right:
            currArea = (right-left) * min(height[left],height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(maxArea, currArea)
        return maxArea

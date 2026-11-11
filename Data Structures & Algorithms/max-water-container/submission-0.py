class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) -1
        maxarea = 0

        while i < j:
            size = j - i 
            minhigh = min(heights[i],heights[j])
            area = size * minhigh
            if area > maxarea:
                maxarea = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxarea

        
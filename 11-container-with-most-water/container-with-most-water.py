class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        PREP
        parameters:
        int list heights
        return:
        int area = w * h 
        max area that can contain water
        example:
        height = [1,8,6,2,5,4,8,3,7]
        return = 49
        pseudocode:
        1. area = 0
           min_height = float('inf')
           left = 0, right pointers
        2. while left <= right
            min left and right
            width = right - left + 1
            area = max(area,  width * min) 
            if left < right :
                left += 1
            else:
                right -=1
        return maxarea
        '''

        max_area = 0
        min_height = float('inf')
        left = 0
        right = len(height) - 1

        while left <= right:

            min_height = min(height[left], height[right])
            width = right - left
            current_area = width * min_height
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return max_area


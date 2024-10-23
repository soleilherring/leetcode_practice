class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        sliding window?
        PREP
        parameters = nums list int
        return = sum of the numbers
        example: [-2, 1, -3, 4. -1, 2, 1, -5, 4] --> 4, -1, 2, 1 sum = 6
        pseudocode:
        curr_sum = nums[0]
        max_sum = 0 
        for num in nums:
            if curr_sum < 0 :
                curr_sum = 0
            curr_sum += num 
            max_sum = max(max_sum, curr_sum)
        return max_sum 
        '''
        
        curr_sum = 0
        max_sum = nums[0]

        for num in nums: #5, 4,-1, 7, 8
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num #23
            max_sum = max(max_sum, curr_sum) #23
        return max_sum 

        # [5,4,-1,7,8]
        # curr_sum = 0
        # max_sum = 0
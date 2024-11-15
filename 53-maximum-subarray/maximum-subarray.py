class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        PREP
        parameters:
        int lst of positive and negative numbers
        return:
        int largest sum of a subarray
        example:
        - nominal:
        [-2,1,-3,4,-1,2,1,-5,4] -> 6 
        - edge case:
        [1] -> 1
        pseudo:
        1. variable. tohold the maximum 
           variable to have the current sum
        2. if the current sum ever becomes equal to zero, restart the current sum
        3. compare the maximum sum to the current sum
        4. return the maximum sum
        '''
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            if curr_sum <= 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum
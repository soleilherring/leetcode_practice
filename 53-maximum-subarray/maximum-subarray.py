class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """PREP
        parameters: 
        int list nums
        return: 
        maximum subarray 
        largest sum
        example:
        [1,2,4,-2, 1] -> 7, [1,2,4]
        pseudocode:
        - two pointers
        -left and right pointer, starting at the first item in the list
        1. declare/initialize variable:
            a. max_sum = 0
            b. left = 0
            c. right (for loop)
        2. for loop moving through array 
            a. for right in range(len..)
                b. if statement 
                    - check if the sum is <= 0, if so, move the left pointer to the right
                c. else
                    - get the max_sum so far
            return max_sum
        """
        max_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum












        
        # '''
        # PREP
        # parameters:
        # int lst of positive and negative numbers
        # return:
        # int largest sum of a subarray
        # example:
        # - nominal:
        # [-2,1,-3,4,-1,2,1,-5,4] -> 6 
        # - edge case:
        # [1] -> 1
        # pseudo:
        # 1. variable. tohold the maximum 
        #    variable to have the current sum
        # 2. if the current sum ever becomes equal to zero, restart the current sum
        # 3. compare the maximum sum to the current sum
        # 4. return the maximum sum
        # # '''
        # max_sum = float('-inf')
        # curr_sum = 0
        # for num in nums:
        #     # if the num is larger than the sum of the curr_sum + num, than we want to start a new subarray count here, otherwise
        #     # if the curr_sum + num is larger, we want to continue with our current subarray
        #     curr_sum = max(num, curr_sum + num) 
        #     max_sum = max(max_sum, curr_sum) 
        # return max_sum
        # # [-2,1,-3,4,-1,2,1,-5,4]

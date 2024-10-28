class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        '''
        Prep
        parameters:
        int array (nums)
        return:
        int: the maximum difference between increasing elements
        example:
        1. [7,1,5,4] -> 4
        2. [10, 3,1]
        pseudocode:
        1. Variables:
        min_num = nums[0]
        max_num = 0
        2. for loop in range len of nums
            a. difference = nums[i] - min_number
            b. calculate the max
            max_num = max(max_num, difference)
            c. min_num = min(min_num, nums[i])
        3. Result
        a. returning max_num
        '''
        min_num = nums[0]
        max_num = 0

        for i in range(1,len(nums)):
            difference = nums[i] - min_num   
            if difference > max_num:
                max_num = difference
            if nums[i] < min_num:
                min_num = nums[i]
        
        if max_num == 0:
            return -1
        else:
            return max_num
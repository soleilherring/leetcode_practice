class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        '''
        PREP
        parameters:
        int nums list
        return:
        int num of the product of subarray
        example
        [2,3,-2,4]-> 6 (2 * 3)
        pseudocode:
       1. prefix and suffix 
       prefix = 1
       suffix = 1
       result = nums[0]
    2. for loop
        if nums[i] == 0:
            prefix = 1
            suffix = 1
        backwards:
        j = len(nums) -i - 1
        prefix *=nums[i]
        suffix *=nums[j]
        pre_suff_max = max(prefix, suffix)
        result = max(result, pre_suff_max )
     return result 
     '''
        prefix = 1
        suffix = 1
        result = nums[0]

        for i in range(len(nums)):
            # backwards 
            j = len(nums) - 1 - i 

            # if prefix or suffix becomes 0 than we need to restart our subarray
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[j]

            # get the max between the prefix and suffix 
            # pref_suff_max = max(prefix, suffix)

            # get the max between the current result and the updated max calculated from pref_suff_max
            result = max(result, prefix, suffix)
        return result

        # # do this in case there is neg and 0, ex : [-2,0], want to return 0
        # res_max = max(nums)
        # min_prod = 1
        # max_prod = 1

        # for n in nums: #2, 3, -2, 4
        #     # create a temporary variable to hold the max product as of now
        #     curr_max = max_prod # 1, 2, 6
        #     # calcualte new max
        #     max_prod = max(max_prod *n, min_prod *n, n) #(2, 2, 2)->2 ; (6, 6, 3)->6; (-12, -6, -2)-> -2; (-8, -48,4 )->4
        #     # calculate new min, using old curr_max that hasn't been updated yet
        #     min_prod = min(curr_max *n, min_prod *n, n) #(2,3, -12, -48)
        #     # check what is max 
        #     res_max = max(res_max, max_prod) #4, 6, 
        # return res_max
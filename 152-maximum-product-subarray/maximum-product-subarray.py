class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # do this in case there is neg and 0, ex : [-2,0], want to return 0
        res_max = max(nums)
        min_prod = 1
        max_prod = 1

        for n in nums: #2, 3, -2, 4
            # create a temporary variable to hold the max product as of now
            curr_max = max_prod # 1, 2, 6
            # calcualte new max
            max_prod = max(max_prod *n, min_prod *n, n) #(2, 2, 2)->2 ; (6, 6, 3)->6; (-12, -6, -2)-> -2; (-8, -48,4 )->4
            # calculate new min, using old curr_max that hasn't been updated yet
            min_prod = min(curr_max *n, min_prod *n, n) #(2,3, -12, -48)
            # check what is max 
            res_max = max(res_max, max_prod) #4, 6, 
        return res_max
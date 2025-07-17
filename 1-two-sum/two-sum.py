class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # parameter
        # 1. list of nums
        # 2. target

        # return the indices of the two numbers such that they add up to target [index1, index2]
        # example:
        # [1, 2, 4, 3] target = 6
        # [1,2]

        # - cannot reuse the same index twice, one solution

        # pseudocode:
        # {
        #     1:0, 2:1, 4:2, 3:3
        # }
        # difference = 6-1 = 5 
        # difference = 6- 2 = 4
        # retun [1, 2]  

        # a. dict key = num, val - index
        # b. loop through each num in array
        #     calculate the difference between the target and n um
        #     if the difference is in the num_index, retrun its value and the current value (index)

        num_index = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_index:
                return [index, num_index[difference]]
            num_index[num] = index 









        # # parameters:
        # # int list of nums
        # # int target 
        # # return array of indexes
        # # example: [2,3,5] target = 8, return: [1,2]
        # # [2,2] target = 4 ! return [0,0] =>[0,1]

        # # psuedo:
        # # array of nums where each index 
        # num_dict = {}
        # for index, num in enumerate(nums):
        #     difference = target - num
        #     if difference in num_dict:
        #         return [index, num_dict[difference]]
        #     num_dict[num] = index  
        # return []

            
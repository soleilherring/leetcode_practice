class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # parameters:
        # int list of nums
        # int target 
        # return array of indexes
        # example: [2,3,5] target = 8, return: [1,2]
        # [2,2] target = 4 ! return [0,0] =>[0,1]

        # psuedo:
        # array of nums where each index 
        num_dict = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference not in num_dict:
                num_dict[num] = index  
            else: return [index, num_dict[difference]]
            
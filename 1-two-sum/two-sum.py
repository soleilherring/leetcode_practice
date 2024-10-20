class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        prep
        p - nums(list) and target(int)
        r - list of indices of the two numbers that add up to target
        e - [2,7,11,5], target = 9, return [0,1]
            [3,3] , target = 6, [0,1];
        p- 
        1. array to hold the result
            difference = 0
        2. for loop, enumerate index, value
            a. variable to hold the difference between the target and the current val
                difference = 9 - 2 -> 7; 
            b. if the current difference is in the array, then append the index of the val and the other number and index != nums.index(difference)
                result.append(index, nums.index(difference))
            *check if the index is already used 
            return array

        '''
        result = []
        difference = 0

        for i, val in enumerate(nums):
            difference = target - val
            if difference in nums and i != nums.index(difference):
                return [i, nums.index(difference)]
                

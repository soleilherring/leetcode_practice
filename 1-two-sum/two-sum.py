class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''PREP
        paramters: 
        int nums list
        int target 
        return: 
        indices of two numbers that add up to target
        example
        [2,7,11,15], 9 -> [0,1]
        - cant have same indices
        [3,3] -> 6 [0,1]
        pseudo:
        1. difference variable  = 0
           dictionary key = element and value is index
        2. make a for loop 
            - for each index, number in enumerate nums
                - calculate differnce
                    difference = target - element
                - if the difference is in the dictionary
                    return index and dictionary[difference]
                -add the element. andindex to the dictionary
                    dictionary[element] = index
        '''
        difference = 0
        ele_indx = {}
        # traditional for loop with range
        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     if difference in ele_indx: 
        #         return [ele_indx[difference], i]
        #     ele_indx[nums[i]] = i 

        # enumerate
        for index, element in enumerate(nums):
            difference = target - element
            if difference in ele_indx:
                return [index, ele_indx[difference]]
            ele_indx[element] = index
                

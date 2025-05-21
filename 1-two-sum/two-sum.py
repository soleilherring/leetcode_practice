class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # PREP
        # 1. parameters:
        # array of nums, 
        # int target 
        # 2. return the indices of the two numbers that added together make the target
        # 3. example:
        #     a. [2,4,5,1] target 9, 
        #     b. return [1,2]
        # 4. pseudocode
        #     a. make a variable to calculate the difference between the target and the current element
        #     b. make a dictionary to hold the numbers
        #     c. for loop to move through each element in the list
        #         a. if the target - element is in the dictionary, return the target index and the index of the other element
        
        difference = 0
        num_index = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_index:
                return [num_index[difference], index]
            num_index[num] = index


 
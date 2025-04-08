from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # PREP
        # 1. parameters: int nums array
        # 2. return boolean (true if duplicate, false otherwise)
        # 3. example: [1,2,3,1] => true (1 repeated)
        # 4. pseudocode:
        # 1. create either dictionary or set
        # 2. if number already exists in dictionary or set, return true, 
        #     at end of loop return false

        # contents = {}
        # for num in nums:
        #     if num in contents:
        #         return True
        #     contents[num] = contents.get(num, 0) + 1  
        # return False 

        # set version:
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False 
        # '''
        # PREP
        # parameters:
        # int nums array 
        # return:
        # true if value appears at least twice
        # false otherwise
        # example:
        # [1,2,3,1]- > true (1 is duplicate)
        # pseudocode:

        # version 1:
        # make a set of the nums list
        # compare the set length vs. list length,
        # if different, return true (because set length will only have distinct numbers so if it differs from length of 
        # nums list, that means we have duplicates)

        # version 2:
        # dictionary
        # if the number is already in the dictionary, return true
        # otherwise, add the number to dictionary
        # return false at end if never finding a duplicate

        # version 3:
        # As move through list
        # if encounter number already in set, return true
        # otherwise, return false at the end

        # '''
        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         return True
        #     num_set.add(num)
        # return False
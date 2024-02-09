from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use dictionary
        # edge case
        # empty or singular item in array

        # dictionary for frequency
        nums_frequency = {}

        for num in nums:
            if num in nums_frequency:
                return True 
            nums_frequency[num] =  1
        return False 
    
        # Version 2

        # return len(set(nums)) != len(nums)

        # Version 3

        # seen = {}
        # for num in nums:
        #     if num not in seen:
        #         seen[num] =1
        #     else:
        #         seen[num]  +=1
        
        # for num in seen.values():
        #     if num >1:
        #         return True
        # return False


        # Version 4
        # first define a set 
        # set_of_letters = set()
        # for letter in nums:
        #     if letter in set_of_letters:
        #         return True
        #     set_of_letters.add(letter)
        # return False

        # Version 5

        # seen = {}

        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen[num] = seen.get(num, 0) + 1
        # return False 

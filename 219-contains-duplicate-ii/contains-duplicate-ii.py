class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #    prep
    #    parameters:
    #    int nums list
    #    int k 
    #    return true is abs(i - j)<=k

    #    example: nums = [1,2,3,1,2,3], k = 2
    #    output: False (because 0-3 = 3 and 3 ! <= k)

    #    pseudocode:
    #     1. make dict
    #         a. key = number
    #         b. value = index
    #     2. check if the key is already in the dict
    #         a. if key in dict subtract abs of index of dict value - current value
    #             return true 
    #     3. return false 
        
        distinct = {}
        for i, num in enumerate(nums):
            if num in distinct and abs(distinct[num] - i) <= k:
                return True 
            distinct[num] =i
        return False 
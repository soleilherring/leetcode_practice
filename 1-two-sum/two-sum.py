class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff not in seen:
                seen[num] = index
            else:
                return seen[diff], index
        
            

            
        
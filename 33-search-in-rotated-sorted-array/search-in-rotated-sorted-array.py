class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        PREP
        parameters:
        int nums list
        return: index of the target value
        -1 if the value isn't in the array
        examples:
        [4,5,6,1,2] ; 1 -> 3
        [1,2,3,0,-1] ; 4 -> -1 
        [1]; 0 -> -1
        pseudocode:
        1. create variables to hold the starting and ending index
            start = 0 
            end = len(nums) -1
        2. while loop start < = end 
            mid = start + end //2 

            # find the pivot
           
         return -1
        '''
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            # check if the target is equal to the nums[mid]
            if target == nums[mid]:
                return mid
            # check left half to be sorted
            if nums[start] <= nums[mid]:
                # check if the target number is in the current range, dont include nums[mid] because we check that
                # with the first if statement
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # if left half isnt sorted than right half must be
            else:
                # check if target is between the nums[mid] and including nums[end], because we did the check of target == nums[mid] with the first check
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1 
      
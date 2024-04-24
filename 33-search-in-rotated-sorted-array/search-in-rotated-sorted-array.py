class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        # start binary search
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle 
            # check start and middle to see if the array is rotated in first half
            if nums[start] <= nums[middle]:
                # check if first part is sorted
                # if it is, the target is within that section of the array 
                if nums[start] <= target < nums[middle]:
                    # limiting search 
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                # checking if second half is sorted
                # if it is, the target is within that section of the array
                if nums[middle] < target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle -1 
        return -1 


      
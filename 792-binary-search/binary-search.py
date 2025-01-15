class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # get start and end index
        # prep
        # 1. get the start and end index
        # 2. make a while loop
        #     a. get a middle index
        #     b. check if that value at the middle index is our target, if so return index
        #     c. elif that value is larget than our target, end= middle
        #     d. else (if value is less than target), start = middle + 1 
            
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return - 1
        
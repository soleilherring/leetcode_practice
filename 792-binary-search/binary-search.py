class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get start and end index
        start = 0
        end = len(nums) - 1

        while start <= end: 
            # middle index
            mid = start + (end - start)//2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1 
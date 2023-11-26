# Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted. 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
def findMaxAverage(self, nums, k):
    window_sum = sum(nums[:k])
    current_max = window_sum/k
    n = len(nums) 
    
    for i in range(n -k ):
        window_sum = window_sum -nums[i] + nums[i + k]
        window_avg = window_sum/k
        current_max= max(current_max, window_avg)
    return current_max
    
    # version 2
def findMaxAverage2(self, nums, k):
    n = len(nums)
    max_avg = 0 
    for i in range(n - k+1):
        window_sum =sum(nums[i :i+k])
        current_avg = window_sum/ k
        max_avg = max(max_avg, current_avg)
    return max_avg
            
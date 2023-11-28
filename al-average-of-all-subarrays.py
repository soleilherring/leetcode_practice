# Average Of All Subarrays - Example Question
# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

# Let’s understand this problem with real input:

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Here is the final output containing the averages of all subarrays of size '5':

# Output: [2.2, 2.8, 2.4, 3.6, 2.8]
def findAverage(nums, k):
    n = len(nums) 
    window_sum = sum(nums[:k])
    window_sum_average = window_sum/ k
    avg_nums = [window_sum_average]

    
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i +k ]
        window_sum_average = window_sum / k
        avg_nums.append(window_sum_average)
    return avg_nums

    # version 2
def findAverage2(nums, k):
    n = len(nums)
    avg_nums = []
    # window
    for i in range(n -k +1):
        window_sum = sum(nums[i:i+k])
        window_sum_avg = window_sum / k
        avg_nums.append(window_sum_avg)
    return avg_nums 
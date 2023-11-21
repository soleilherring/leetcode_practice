# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        count = 0 
        window_sum = sum(arr[:k])
        window_avg = window_sum/k
        
        if window_avg >= threshold:
            count +=1
        
        n = len(arr)
        for i in range(n-k):
            window_sum = window_sum - arr[i] + arr[i+k]
            window_avg = window_sum/k
            if window_avg >= threshold:
                count+=1
        return count 
    
    # Version 2
    # count = 0
    #     for i in range(len(arr) - k+1):
    #         window_sum = sum(arr[i:i+k])
    #         window_avg = window_sum/k
    #         if window_avg >= threshold:
    #             count +=1
    #     return count
        
            
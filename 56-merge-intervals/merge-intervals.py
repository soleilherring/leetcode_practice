class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        # parameters:
        # intervals
        # array or int arrays
        # output the merged interval
        # array of int arrays
        # note:
        # if the numbers are the same they are overlapping intervals

        # 1. result array
        # 2. add the first interval from intervals into the result array
        # 3. for loop starting at 1 up to length of intervals
        #     a. unpack the two numbers start end
        #     compare if start <= end of the previous(currently in result) array 
        #         if so, replace the last digit of the previous(in result) with the maximum of the ends of curr and previous
        #     otherwise, append the entire array
        # return result 
        
        # sort first to assume we can always have the first number as the starting value
        intervals.sort( key = lambda interval : interval[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            start, end = interval
            if start <= result[-1][1]:
                max_end = max(result[-1][1], end)
                result[-1][1] = max_end
            else:
                result.append([start,end])
        return result 






























        # # want to have an result array
        # # sort the array by the 1st number in each subarray
        # # check the last number in the result array [-1][1] vs. first number in the current arary
        # # if the first number in the current array is less than last number, we know it can be merged
        # # check which value is greater, the last digit in the current array or the last digit in the subarray 
        #     # if the number is greater in the current array, replace the subarray's last number with the current subarrays last number

        # result = []
        # # sort the arrays in the intervals by the first number
        # intervals.sort(key = lambda interval : interval[0])
        # # add the first item in intervals to the result array so we can compare against something
        # result.append(intervals[0])

        # for start, end in intervals[1:]:
        #     prev_end = result[-1][1]
        #     # if the start value is less than the prev end that means they overlap
        #     # example [[3, 5], [4, 9]] -> [3,9]
        #     if start <= prev_end:
        #         # we know that we can merge
        #         # need to check which is greater, the end or the last value in the interval in result
        #         max_end = max(prev_end, end)
        #         result[-1][1] = max_end
        #     else:
        #         result.append([start,end])
        # return result
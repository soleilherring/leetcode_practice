class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if each number is start number, by checking if one less in array
        num_set = set(nums)
        longest = 0 
        for num in num_set:
            if num - 1 not in num_set:
                current_length = 1
                while num + current_length in num_set:
                    current_length += 1
                longest = max(longest, current_length)
        return longest 


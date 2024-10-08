class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # make a set to hold unique values
        # variable to hold max count of chars so far
        # make left pointer
        # for loop to iterate through len of list
        # while loop to check if the letter is in the set
        # if in the set remove the letter from the set and increment left pointer 
        # if not in set, add it to set
        # calculate the max count so far by comparing our current max count and the index of r - l + 1. We do this because we want to find the difference in length, which gives us how many characters, but add one since we want it to be inclusive of our index
        # return the max

        unique = set()
        max_count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1 
            unique.add(s[r])
            max_count = max(max_count, r - l + 1)
        return max_count 
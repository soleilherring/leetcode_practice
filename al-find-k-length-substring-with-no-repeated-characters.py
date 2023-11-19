# Find K-Length Substrings With No Repeated Characters
# Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

# Example 1:

# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
# Example 2:

# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

class Solution:
    def numKLenSubstrNoRepeats(self, s, k):

        if k > len(s):
            return 0
        
        n = len(s)
        count = 0
        window = s[:k]
        distinct = set(window)

        if k == len(distinct):
            count +=1 
            
        for i in range(n-k):
            
            window = window[1:] + s[i+k]
            distinct = set(window)
            if len(distinct) == k:
                count +=1 
                
        return count 

        # alternative version
        # if k > len(s):
        #     return 0
            
        # n = len(s)
        # count = 0
        
        # for i in range(n-k+1):
        #     window = s[i:i+k]
        #     distinct = set(window)
        #     if len(distinct) == k:
        #         count +=1 
        # return count 
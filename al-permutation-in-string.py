# Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.

# option 1
from collections import Counter 
class Solution:
    def checkInclusion(self, s1, s2):
        n = len(s2)
        k = len(s1)
        
        if k > n:
            return false
            
        # make window
        window = s2[:k]
        
        s1_counter = Counter(s1)
        s2_counter = Counter(window) 
        
        if s1_counter == s2_counter:
            return True
        
        for i in range(n - k):
            window = window[1:] + s2[i+k]
            if s1_counter == Counter(window):
                return True
        return False 
        
    # option 2:
    # s1_map = Counter(s1)
            
        # for i in range(n-k+1):
        #     s2_map = Counter(s2[i:i+k])
        #     if s1_map == s2_map:
        #         return True
        # return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

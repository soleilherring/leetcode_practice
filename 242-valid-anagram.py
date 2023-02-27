# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a dictionary
        # if the letter is not in dictionary add it to dictionary and check if other word has same number of letters, if not, return false
        s_dict = {}
        t_dict = {}
        # check if the two words don't have the same number of words
        if len(s) != len(t):
            return False 

        for letter in s:
            if letter not in s_dict:
                s_dict[letter] =1
            else:
                s_dict[letter] +=1
        
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] =1
            else:
                t_dict[letter] +=1

        if s_dict != t_dict:
            return False
        else:
            return True 


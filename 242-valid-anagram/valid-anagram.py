from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # paramsters:
        # two strings
        # s 
        # t

        # return true or false

        # for each letter, check if it is in the other word's dictionary. if it is, subtract that letter from the dictionary
        # at the end check if the dictionary has any non 0 value, if so return false

        # or
        if len(t) != len(s):
            return False

        letters_in_s = Counter(s)

        for letter in t:
            if letter in letters_in_s:
                letters_in_s[letter] -= 1
            

        for count in letters_in_s.values():
            if count != 0:
                return False
        return True 























        # parameters: 
        # s string of chars
        # t string of chars
        # return boolean (true if t is anagram of s)
        # 1. check if they are of different lengths, return false
        # 2.  sort and then compare?
        # 3. if they are the same, return true otherwise false
        # # comapre the sorted viersions
        # return sorted(s) == sorted(t)/\

        # dictionary for s with key as letter and value as count. loop through t and deduct when it's in the dct andd if lterr is not in dict return false

        # s_count = Counter(s)

        # for letter in t:
        #     if letter not in s_count:
        #         return False
        #     s_count[letter] -=1

        # for val in s_count.values():
        #     if val != 0:
        #         return False
        # return True

        
        
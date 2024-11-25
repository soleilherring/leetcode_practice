class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        PREP
        parameters:
        s string
        t string
        return:
        true or false
        true if anagram(letters in different order can make same word)
        example
        "anagram" ; "nagram" -> true
        "rat" ;"car" -> false
        "sl" ; "s" -> false
        ''; '' -> true
        pseudo:
        1. create a hashmap
        have a count of the letter in one string
        have a deduction of the letter of the same character in the other string
        if they become zero, than we found the same number of strings in both string
        2. if there is a non zero value in the dictionary, that means one or more of the characters appears 
        multiple times, so they are not anagrams
            return  false
        '''
        if len(s) != len(t):
            return False

        s_count = {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            s_count[t[i]] = s_count.get(t[i], 0) - 1
        # count the values, and they should cancel each other out if they have the same letters and are anagrams
        # otherwise, if they are any extra letters the value of the dictionary will not be 0 and we will return false
        for val in s_count.values():
            if val != 0:
                return False
        return True 


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
        # if len(s) != len(t):
        #     return False

        # s_count = {}
        # for i in range(len(s)):
        #     s_count[s[i]] = s_count.get(s[i], 0) + 1
        #     s_count[t[i]] = s_count.get(t[i], 0) - 1
        # # count the values, and they should cancel each other out if they have the same letters and are anagrams
        # # otherwise, if they are any extra letters the value of the dictionary will not be 0 and we will return false
        # for val in s_count.values():
        #     if val != 0:
        #         return False
        # return True 

        #################### version two using ord()
        '''
        pseudo
        1. have an array with 26 spots for each letter in the alphabet
            assume the letters are lowercase in this instance
        2. for each letter in s find it's ord number by subtracting its ord number from letter a
        this will tell us the index postion to put the count at
            example:
            x = 'z'
            count = 26 * [0]
            for x in s:
                count[ord(x) - ord('a')] += 1 
                *** same as count[122 - 97] += 1
                            count[25] += 1
                            [0.......1]
        3. loop through the count
            if there are any values !=0, return false, otherwise true

        '''
        count = [0] * 26 #making. anarray with 26 positions with 0 as the frequency at that position
        for letter in s:
            count[ord(letter) - ord('a')] += 1 #subtract the unicode number from a, since only 26 letters in alphabet will get a index to place the frequency of the letter in the array

        for letter in t:
            count[ord(letter) - ord('a')] -= 1 #finding the unicode number again to find the count of letter in the count aray and then deducting it

        for frequency in count: #since the anagram is assumed to have the same number of letters we should cancel them out by subtracting, them. if not 0, its false
            if frequency != 0:
                return False
        return True


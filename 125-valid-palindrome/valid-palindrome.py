class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # i = 0 
        # j = len(s) - 1 
        # print(s)
        # while i < j:  
        #     while i < j and not s[i].isalnum():
        #         i += 1
        #     while i < j and not s[j].isalnum():
        #         j -= 1
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1 
        #     j -= 1
        # return True 
            
        ######### other approach, get the string, remove spaces/non alpha numeric characters, compare to its reverse
        # list comprehension, join
        letters = ''.join([letter.lower() for letter in s if letter.isalnum()])
        return letters == letters[::-1]

        

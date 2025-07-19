from collections import deque 
class Solution:
    def reverseWords(self, s: str) -> str:

        q= deque([])
        
        left = 0

        while left < len(s):
            word = ''

            while left <len(s) and s[left] == " ":
                left += 1

            while left <len(s) and s[left] != " ":
                word += s[left]
                left += 1
            
            if word:
                q.appendleft(word)
                left += 1

        return " ".join(q)

            




































        # parameter: 
        # string of characters separated by a space. 
        # - might include multiple spaces
        # return reversed string with only one space between each word
        # - example: 'i love pizza ' -> 'pizza love i'

        # 1. join with , 
        # 2. reverse the array ^
        # 3. split again with spaces 


        # result = []
        # i = len(s) -1
        # while i >= 0:
        #     letters = ''

        #     while i >= 0 and s[i] == ' ':
        #         i -= 1

        #     if i < 0:
        #         break

        #     while i >=0 and s[i].isalpha():
        #         letters = s[i] + letters
        #         i -= 1

        #     result.append(letters)
            
        # return " ".join(result)     
                



            
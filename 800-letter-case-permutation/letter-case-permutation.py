class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # dfs because each letter has two options to choose from, lowercase or uppercase
        # if not letter, continue and add the number to the current string youre building

        # string of characters/numbers
        # return an array of strings, every possible string we could create
        # pseudo
        # 1. have a final result array that will be outside of the dfs 
        # 2. have a dfs that has 
            # step 1:
            # initialize/declare an empty string that wil be later added to result array
            # sub_res = ''
            # a. base case where the  i is the length of s
            #     return 
            # b. recursive cases
            #     i. check if alphabetical
            #         -lowercase
            #         -uppercase
            #     ii. numeric 
            # append the string to the result??
        result = []
       
        def dfs(i, path):
            # base case
            if i == len(s):
                result.append(path)
                return 

            # recursive case
            # check if alpha
            if s[i].isalpha():
                # lower
                dfs(i + 1, path + s[i].lower())
                # upper
                dfs(i + 1, path + s[i].upper())
            # numeric
            else:
                dfs(i + 1, path + s[i])

        dfs(0, '')
        return result 
      
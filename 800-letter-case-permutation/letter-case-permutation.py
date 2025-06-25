class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        PREP
        parameters: string 
        return
        list of strings
        example:
        [a1B2, a1B2, A1b2, A1B2]
        pseudocode
        1. get the 
    
        """
        final = []
        result = ""
        # dfs backtracking
        def dfs(index, result):
            #  base case
            if index == len(s):
                return final.append(result)
            # let\ter 
            if s[index].isalpha():
                # lowercase
                dfs(index + 1, result + s[index].lower())
                # uppercase 
                dfs(index + 1, result + s[index].upper())
            # number (just append it)
            else:
                dfs(index + 1, result + s[index])
        
        dfs(0,"")
        return final
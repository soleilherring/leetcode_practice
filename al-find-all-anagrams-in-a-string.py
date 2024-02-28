class Solution:

    def createDict(self, str_value):
        char_dict = {}
        for letter in str_value:
            if letter not in char_dict:
                char_dict[letter]= 1
            else:
                char_dict[letter] +=1
        return char_dict

    
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # make dict for p and s
        p_dict = self.createDict(p)
        s_dict = self.createDict(s)
        # get k length of p
        len_p = len(p)
        len_s = len(s)

        # make array to hold the indices
        result = []

        # check if leng of p is greater than s
        if len_p > len_s:
            return []
        for i in range(len_s - len_p +1):
            window = s[i: i+len_p]
            s_dict = self.createDict(window)
            if s_dict == p_dict:
                result.append(i)
        return result 


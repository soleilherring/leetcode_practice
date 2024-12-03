class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''PREP
        parameters;
        s string 
        p string
        lowercase alphabetical english characters
        return:
        list of startign indices of the anagrams from p in s
        example:
        s= "abcdefgabc"
        p= "abc"
        [0,7]
        s = "ab"
        p = "abc"
        []
        pseudocode:
        0. list variable, window variable, k variable (len of p)
        1. sliding window starting and ending pointers of window size 
        p_sorted variable 
        2. when at a subwindow, check if it is the same as the sorted p
            if not sorted, recalculate window
            else: append the starting index to the list
        3. return list
        '''
        k = len(p)
        n = len(s)
        result = []
        window = s[:k]
    

        # print(letter_freq(window))/
        p_counter = collections.Counter(p)
        w_counter = collections.Counter(window)
        start = 0 
        end = k -1 

        for i in range(n-k+1):
            if w_counter == p_counter:
                result.append(start)

            w_counter[s[start]] -=1
            if w_counter[s[start]] == 0:
                del w_counter[s[start]]
            start += 1

            if end + 1 < n:
                end +=1 
                w_counter[s[end]] += 1
            # if start + k < n:
            #     w_counter[s[start  + k ]] += 1
            
        return result 

        
        # "cbacadac" "ac" -> [2,3,6]
        #  p_alpha_order= 'ac'
        #  index = 3
        #  sorted_window = "ac" 
        #  window = "ca"
        #  result [2,3]


    #     char_dict = {}
    #     for letter in str_value:
    #         if letter not in char_dict:
    #             char_dict[letter]= 1
    #         else:
    #             char_dict[letter] +=1
    #     return char_dict

    
    # def findAnagrams(self, s: str, p: str) -> List[int]:

    #     # make dict for p and s
    #     p_dict = self.createDict(p)
    #     s_dict = self.createDict(s)
    #     # get k length of p
    #     len_p = len(p)
    #     len_s = len(s)

    #     # make array to hold the indices
    #     result = []

    #     # check if leng of p is greater than s
    #     if len_p > len_s:
    #         return []
    #     for i in range(len_s - len_p +1):
    #         window = s[i: i+len_p]
    #         s_dict = self.createDict(window)
    #         if s_dict == p_dict:
    #             result.append(i)
    #     return result 


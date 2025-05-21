class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        PREP
        parameters:
        string s
        string t
        return:
        string of min window substring 
        example:
        s = "ABCDEYFGHIJK" t = "EFG
        return "EYFG"
        pseduocode:
        1.check if the t is longer than s, return ""
        2. left = 0 and right pointer(for loop)
            min_string = float('inf')
        3. dictionary for s and t
            add the letter do the dictionary from right as long as the current num of abc != length of t
            if the current_num of abc == t_length, then check its r-l+1 to the current min_string
                deduct from the left while the current_length == t_length, if it's not add from the right
        4. return the min string

        '''
        left = 0
        current_num = 0
        current_dict = collections.Counter()
        min_string = float('inf')
        letters = ""
        t_dict = collections.Counter(t)
        t_length = len(t_dict)

        if len(t) > len(s):
            return ""

        for r in range(len(s)):
            # want to check if our current letter is one of the letters in t_dict
            if s[r] in t_dict:
                # if letter in t_dict, +=1 to current_dict 
                current_dict[s[r]] += 1
                # check if the curretn_dict[s[r]] == t_dict[s[r]] because than we know we have the correct 
                # counts of the letter (in case there are duplicates of teh same letter)
                if current_dict[s[r]] == t_dict[s[r]]:
                    # if we have the correct count of our letter in both the current_dict and t_dict that means we 
                    # can increment our current of having found the number of times of that uniquehat unique letter
                    current_num += 1
                
            # while we have the current_num == t_lenght (so while we have found all the unique characters in t in s)
            while current_num == t_length:
                # we check if the min_string is greater than our current width of our window, if it is update
                if min_string >  r - left + 1:
                    min_string = r - left + 1 
                    # get the current letters that are the min string
                    letters = s[left:r+1]
                # we will begin to remove left most letter to shrink the window
                # first we check if the left most letter is in the t_dict
                if s[left] in t_dict:

                    # if the s[left] letter frequency is equal in both current_dict and t_dict 
                    # that means that if we remove s[left] from the window the current_num will need to decrease and the window will be invalid
                    if current_dict[s[left]] == t_dict[s[left]]:
                        current_num -=1 
                    # regardless, reduce s[left] -= 1
                    current_dict[s[left]] -=1
                # move the left pointer forward to narrow window
                left +=1

        return letters

            
            


          
            


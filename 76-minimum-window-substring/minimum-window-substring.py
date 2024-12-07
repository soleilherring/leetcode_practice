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
            if s[r] in t_dict:
                current_dict[s[r]] += 1
                if current_dict[s[r]] == t_dict[s[r]]:
                    current_num += 1
                
            while current_num == t_length:
                if min_string >  r - left + 1:
                    min_string = r - left + 1 
                    letters = s[left:r+1]

                if s[left] in t_dict:
                    if current_dict[s[left]] == t_dict[s[left]]:
                        current_num -=1 
                    current_dict[s[left]] -=1
                
                left +=1

        return letters

            
            


          
            


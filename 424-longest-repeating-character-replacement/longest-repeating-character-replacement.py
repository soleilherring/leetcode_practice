class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        PREP:
        parameters: 
        string s
        integer k
        return:
        int of the lenght of the longest substring containing the same lette you can get after choosing any charater of the string and changing it to any other uppercase english chracter
        example
        "ABAB" , k = 2 -> "AAAA" or "BBBB" -> 4
        psedocode:
        1. sliding window 
        pointer at 0th position
        max string 
        2.
        counter dictionary taking into account the number of occurences for current letters
        3. whichever letter has more count, check if the (window size - current max frquency char ) the substring is less than k, that means. wecould continue, otherwishe we have more character to change than we have replacements so we need to shrink the iwndow by deducting from the left most character and also moving in the left most charcter to the right to shrink the string length   
        4. compare the maximum of the length we have seen so far and the current lenght if it is valid
        5. return maximum length
        '''
        max_length = max_freq = 0
        left = 0
        count = {}
        # for loop with right pointer moving through the length of s
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1

            current_length = right - left + 1
            max_freq = max(max_freq, count[s[right]])
            # alternative

            # if max_freq + k >= current_length:
            if current_length - max_freq <= k:
                max_length = max(max_length, current_length)

            else:
                count[s[left]] -=1
                left += 1
        return max_length 
        # Example:
            # # the current length minus our current majority element example
            # "AABBC" k = 2
            #  l   r
            # "A:2"
            # B:2
            # C: 1
            # current_length = 5 
            # max_freq = 2
            # calculation : 5 - 2 = 3 
            # 3 !<= 2, so need to move left forward
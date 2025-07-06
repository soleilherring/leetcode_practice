class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 'a b c a b c b b'
        #                s
        #                r 
        # set = {a}
        # max_length = s:r+ 1 -> 3
        # # if the letter is in the set, remove it from the set and adjust the start

        # 'p w w k e w'
        #      l
        #            r  
        # set { w k e}
        # max substring so far : s[l : r ] => 3
        
        l = 0
        unique = set()
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[l])
                l+= 1
            unique.add(s[right])
            max_length = max(max_length, len(unique))
        return max_length
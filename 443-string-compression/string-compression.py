class Solution:
    def compress(self, chars: List[str]) -> int:
        # parameters:
        # string of characters
        # return a 'compressed' array with the letter and the number next to it
        # if it's only 1 letter, no number
        # more than 9, take up the space next to the letter to put the number
        # return same array

        start = 0
        write = 0
        while start < len(chars):
            r = start
            while r < len(chars) and chars[r] == chars[start]:
                r+= 1
            
            # break out of loop
            # need to rewrite the character and the number after it
            chars[write] = chars[start]
            write +=1
            count = r - start

            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1
            start = r

        return write

#  ["a","2","b","2","c","3","c"]   
                    #  s
                    #         w
                    #              r










    #     parameters: 
    #     list of characters
    #     return is length of compressed string (inplace)
    #     note : 
    #     - if length is 1, just append the character 
    # #     - if length of character count >= 10, split into multiple characters
    # #     pseudocode
    #     s = 0 
    #     write = 0
    #     while s < len(chars):
    #         # our i is moving so we initially start it at same spot as s, when we get to a new letter we will want it 
    #         # to start at whereverr i is again
    #         i = s
    #         while i < len(chars) and chars[i] == chars[s]:
    #             i+=1 

    #         count = i - s 
    #         chars[write] = chars[s]
    #         write += 1

    #         if count > 1:
    #             for num in str(count):
    #                 chars[write] = num
    #                 write += 1 
            
    #         s = i 

    #     return write
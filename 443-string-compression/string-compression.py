class Solution:
    def compress(self, chars: List[str]) -> int:
    #     parameters: 
    #     list of characters
    #     return is length of compressed string (inplace)
    #     note : 
    #     - if length is 1, just append the character 
    #     - if length of character count >= 10, split into multiple characters
    #     pseudocode
        s = 0 
        write = 0
        while s < len(chars):
            # our i is moving so we initially start it at same spot as s, when we get to a new letter we will want it 
            # to start at whereverr i is again
            i = s
            while i < len(chars) and chars[i] == chars[s]:
                i+=1 

            count = i - s 
            chars[write] = chars[s]
            write += 1

            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1 
            
            s = i 

        return write
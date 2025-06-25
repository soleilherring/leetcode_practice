class Solution:
    def compress(self, chars: List[str]) -> int:
        # so two pointers
        # read and write. read is moving to the right to see if the value is same 
        # we could have a variable calle 'start' which tells us where the group starts
        # write will replace whats there with the count + 1

        start = 0
        write = 0

        for r in range(len(chars)):
            if len(chars) == r+ 1 or chars[r] != chars[r+1]:
                chars[write] = chars[r]
                count = r -start+1
                write +=1
                start = r+ 1 
                if count > 1:
                    for num in str(count):
                        chars[write] = num
                        write += 1 
        return write



        
            



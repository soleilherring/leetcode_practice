class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # parameters:
        # array of strings
        # output is longest common prefix

        # find the shortest length word

        # for every letter in that shortest length word
        # check if it each letter in shortest appears in the word
        # once it doesnt, return it 

        shortest  = sorted(strs, key = len)[0]
        print(shortest)

        for i in range(len(shortest)):
            for word in strs:
                if shortest[i] != word[i]:
                    shortest = word[:i]
                    return shortest
        return shortest
        print(prefix)





























        # # parameter 
        # list of strings
        # return the lonest common prefix
        # example:
        # 'carpet', 'car', 'carpenter' -> car 
        # psuedocode:
        # 1. find the shortest word in the string array
        # 2. for each word in strs, move through each word and see if it mathes the letters in the stortest                                                                     
        # word 
        # 3. save the longest prefix in another variable
        # 4. when we hit the longest substring break out of the loop and return it. 

        # # min 
        # shortest = min(strs, key = len)

        # # for i in range(len(strs)):

        # #     while not strs[i].startswith(shortest):
        # #         shortest = shortest[:-1]
        # # return shortest

        # # second way

        # for i in range(len(shortest)):
        #     for word in strs:
        #         if word[i] != shortest[i]:
        #             shortest = shortest[:i]
        #             return shortest
        # return shortest #add this so in case there are never mismatches and the entire prefix is in the word
       


    

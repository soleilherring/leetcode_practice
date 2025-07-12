from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make an array with the 26 letters in. thedictionary 
        # we will count the occurence of each letter and put it in the array
        # [0, 0]
        #  a. b...
        # #  make these into a tuple then set them as the key to a dictoanry
        #      if a word when made into this occurence array is in the dictionary, has this many letters 
        #         it will be the value (append the word the result value )
        # return the result 

        # create frequency array

        anagrams = defaultdict(list)

        
        for word in strs:
            # calcuated for that word the number of times its letters occur
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1

            # tuples are immutable so convert list into tuple and make it a key in the dict
            key = tuple(freq)
            # if key in anagrams:
            #     anagrams[key].append(word)
            # else:
            #     anagrams[key] = [word]
            anagrams[key].append(word)
        return list(anagrams.values())

        
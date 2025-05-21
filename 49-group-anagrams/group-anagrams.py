from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        PREP
        parameters:
        array of strings
        return:
        list of lists with anagrams grouped together
        example:
        ["can", "nap", "pan", "lap", "now", "pal"]
        [["can"], ["nap", pan], ["now"], ["lap", "pal"]]
        pseudo:
        1. make a dictionary 
           make an array to hold the count of each letter at that index (index 0 is letter a, the count of  'a' chars would be there)
           use ord()
        for each word count how many times the letters appear
        2. in result dictionary, have the tuple(count) as the key and the word list is the value. 
        '''
        result = defaultdict(list)
        # m = number of strings
        # n = lenth of each str
        for word in strs: 
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            result[tuple(count)].append(word)
        return list(result.values())

        # Time: O(m * n) 
        # Space: O(m * n) space complexity because in the worst case each word is unique and we have list of lists containig all strings

# old version
        # make a dictionary to hold the words
        # interate through the list of words and sort the letters in the word
        # if the letter sorted in the word is already in dictionary, add the unsorted word to dictionary if not, add just the word 
        # # return list of words
        # if not strs:
        #     return [strs]
        # # word is key and value will default to list
        # anagram_dict = defaultdict(list)

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     anagram_dict[sorted_word].append(word)
        
        # return list(anagram_dict.values())
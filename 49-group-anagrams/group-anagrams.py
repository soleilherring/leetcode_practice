class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # paramters:
        # list of words
        # return an array of anagrams grouped together

        # use ord? use dict and ord?
        # 1. for every word 
        #     for every letter, count the letter and it's index will be teh letter in tthe array and count will be the elemnt
        #     make that the key to the anagrams dict
        #     for every word check if it's list is already in the anagram key, if it is, append tha tword
        #     return the anagrams.values()

        anagrams = collections.defaultdict(list)
   
        # key =( [letters count]) =word list
        for word in strs:
            word_count = [0] * 26
            for letter in word:
                word_count[ord(letter) - ord('a')] += 1

            tuple_word_count = tuple(word_count)
            if tuple_word_count not in anagrams:
                anagrams[tuple_word_count].append(word)
            else:
                anagrams[tuple_word_count].append(word)
        return list(anagrams.values())

            


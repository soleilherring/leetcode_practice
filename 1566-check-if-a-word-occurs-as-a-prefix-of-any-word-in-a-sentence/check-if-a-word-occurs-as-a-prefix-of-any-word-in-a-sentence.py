class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        '''
        parameters:
        string of words -> sentence
        string of characters -> searchWord
        
        return 
        index + 1 of the word that has the searchWord as a prefix
    
        example:
        "we love to eat tacos"
        ea
        return 4

        if searchword not in sentence, return 
        -1

        pseudocode
        split sentence into words
        window of size searchWord
        if searchWord == window for each word, return it's index + 1
        '''

        split_sentence = sentence.split(" ")
        k = len(searchWord)

        for index, word in enumerate(split_sentence):
            # if len(word) < k:
            #     continue
            if word[:k] == searchWord:
                return index + 1
        return -1
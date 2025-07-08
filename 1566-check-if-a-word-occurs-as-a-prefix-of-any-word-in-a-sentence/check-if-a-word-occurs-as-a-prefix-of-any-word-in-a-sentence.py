class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # parameter: 
        # string sentence with  spaces
        # string with a prefix 
        # return the index + 1 of the prefix word in the string ,only can be at start
        # example: "she eats cherry and peachey pies" searchWord = 'che'
        # psuedo:
        # 1. split the string into words within an array separated by a comma
        # 2. use the search word to check the first len(searchword) positions in the word,
        #     if the searchword == word[:len(searchword)]
        #         return the index + 1 //because 1 indexed
        #  3. return -1 //no prefix in string

        window = len(searchWord)
        split_sentence = sentence.split(" ")

        for index, word in enumerate(split_sentence):
            if word[:window] == searchWord:
                return index + 1
        return -1 
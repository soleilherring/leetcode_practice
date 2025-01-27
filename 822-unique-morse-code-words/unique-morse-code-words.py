class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # PREP
        # parameter: list of morse code characters (dots /dashes)
        # return number of unique translations 

        # example: 
        #  words = ["gin","zen","gig","msg"]
        #  output = 2 

        #  pseudocode:
        #  1. create a dictionary
        #  2. create a set of unique morse code

        #  1. map each letter in the alphabet to the morse code (lowercase)
        #  2. main function will return set
        #      (helper function) for each letter in each word, create a string of it's morse code
        #  check if that morse code is already in set, if it is dont do anything, otherwise add it to the set

        #  return length of the set 

        # create mapping of letters to morse code
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_to_alp = {}
        for i in range(len(morse_code)):
            morse_to_alp[chr(97 + i)] = morse_code[i]

        # helper function
        def code(word, decoded_dict):
            coded = []
            for letter in word:
                coded.append(morse_to_alp[letter])
            return ("".join(coded))

        # main function
        unique = set()
        for word in words:
            decoded = code(word, morse_to_alp)
            if decoded not in unique:
                unique.add(decoded)
        return len(unique)

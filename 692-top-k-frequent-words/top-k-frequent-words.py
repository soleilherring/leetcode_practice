class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # parameter: 
        # array of strings
        # int k (number of most frequent words)
        # return:
        # array of k most frequent words
        # - note to sort by lexicographical order if needed
        # - descending order otherwise

        # 1. declare /initialize a counter dictionary
        # 2. if the value (count) is the same for k top number of words, sort lexicographically
        # otherwise, return 
        count_words= {}
        for word in words:
            count_words[word] = count_words.get(word, 0) + 1 
        
        max_count = 0
        max_word = []
        freq = [ [] for _ in range(len(words)+1)]

        for word, count in count_words.items():
            # cat, dog, dog, rover, rover
            # [[], [cat], [dog, rover], [],[],[]]
            #    0.    1.     2
            
            freq[count].append(word)
        # move backwards through the freq array and skip if empt
        # check if the array len is same as k, if so sort and get the array
            # otherwise continue grabbing the words within the arry and add to result array 

        result = []
        for i in range(len(words) -1, 0, -1):
            if freq[i]:
                for word in sorted(freq[i]):
                    result.append(word)
                    if len(result) == k:
                        return result




                


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        parameters:
        list of strings
        return: 
        array of the k most frequent strings in lexicographical order
        pseudo:
           [ ,   ,[i, love],  ]
            0  1. 2

        1. dictionary 
        2. list of lists that occurs the same number of the len of words 
        3. for loop for each word in the dictionary 
            add it's count as the position in the above array 
        4. loop backwards as long as the len of the array > 0. and do it up to k times or while len of the array < len k
    
        """
        counter = Counter(words)

        frequency = [[] for word in range(len(words) + 1)]

        for word, freq in counter.items():
            frequency[freq].append(word)
        
        result = []
        for words in range(len(frequency) -1, 0, -1) :
            if not len(frequency[words]):
                continue 
            frequency[words].sort()
            for word in frequency[words]:
                result.append(word)
                if len(result) == k :
                    return result


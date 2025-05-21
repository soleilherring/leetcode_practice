class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # start
        # end
        start = 0 
        end = len(letters) -1

        if target >= letters[end] or target < letters[start]:
            return letters[start]

        while start <= end:
            middle = start + (end - start) // 2
            
            if target >= letters[middle]:
                start = middle + 1
            else:
                end = middle - 1

        return letters[start]
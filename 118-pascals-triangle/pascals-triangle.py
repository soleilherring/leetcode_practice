class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ 
        prep
        1. parameters:
        int number of rows
        return the rows where each number is the sum of the two numbers directly aove it. 
        example:
        numRows = 3 
        [[1],[1,1],[1,2,1]]
        *always 1 on the outside
        pseudocode:
        1. make a result array with 
        [[1], [1,1]]
        make a new array, add 1 and then add the whatever is in the above array and then append it 
        add 1 to the end
        """

        if numRows == 1:
            return [[1]]
        
        result = [[1]]

        for i in range(1,numRows):
            inner = [1]
            prev = result[-1]
            for j in range(1,len(prev)):
                inner.append(prev[j] + prev[j-1])
            inner.append(1)
            result.append(inner)
        return result
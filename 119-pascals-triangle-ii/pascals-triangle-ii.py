class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        PREP
        parameters; index int
        return: row of nums (list)
        exammple
        rowIndex = 2
        return [[1,2,1]]
        psueodcode:
        1. edge case:
            rowIndex == 0 [1]
            rowIndex == 1, return [1,1]
        2. declare/initialize list 
            [1]
            for loop, range(indexRows +1)
                row = [1]
                for loop, range(1, list[-1]))
                    list[-1][j] + list[-1][j-1]
                    append it to the row,
                append(1)
            return result[-1]
        """

        # first handle edge cases
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        # declare a variable to contain the outside list
        result = [1]
        # make a for loop to handle the iterations rowIndex + 1
        for i in range(rowIndex):
            row = [1]
            prev = result
            for j in range(1, len(prev)):
                row.append(prev[j] + prev[j-1]) 
            row.append(1)
            result = row
        return result          
            

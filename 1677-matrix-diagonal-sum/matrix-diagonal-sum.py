class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        PREP
        parameters; list of integer
        return: sum of the diagnols 
        example:
        [[1,2,3],
        [4,5,6],
        [7,8,9]]

        [[1,1,1,1, 2],
         [1,1,1,1, 2],
         [1,1,1,1, 2],
         [1,1,1,1, 2]]
        pseudo:
        1. iterate through matrix
            a. nest loop
            b total variable
            for i in range(len(mat)):
                j = len(mat) -i - 1
                total += mat[i][i]
                total += mat[i][j]


        2. if odd, find the number in the middle that is added twice
            a. divide down the middle of the list of lists (len(mat) -1 + 0 //2) _> indexof the middle
            b. find the middle number and subtract it from the sum 
        3. return total
        '''
        total = 0
        for i in range(len(mat)):
            j= len(mat) - 1 -i
            total += mat[i][i]
            total += mat[i][j]
        # odd length of matrix/sublists
        if len(mat) %2 :
            middle = len(mat) //2
            total -=mat[middle][middle]
        return total




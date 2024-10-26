class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        '''
        prep
        parameters; list of lists
        return: true or a false
        - true if the  elements in the diagnol are non-zero
        - true if the elments in the middle and end are 0 
        example:
        grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
        return true 
        grid = [[5,7,0],[0,3,1],[0,5,0]]
        return false
        pseudo:
        1. make a for loop to check the diagnol starting on left side and right side are non zeor
            a. for i in range(len(grid)):
                for j in range(len(grid)):
                    i. check if the i & j are the same so (0,0), (1,1), (2,2) t
                    or if j = len(grid) - i -1 (that means the other diagnol)
                    (0,2), (1, 1), (2,0) == 0:
                        return false
                    
                    ii. check if the mat[i][j] !=0 return false
            

            b. return True

        '''
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i == j or j== len(grid) -i-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] !=0:
                        return False
        return True 
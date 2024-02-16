class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        # column
        # 3x3 
        # for i in range(rows):
        #     row_set = set()
        #     if board[i][i] != "." and board[i][i] not in row_set:
        #         row_set.add(board[i][i])
        #         print(row_set)
        #     else:
        #         print(row_set)
        #         return False 
        
        # return True 
        
        res =set()
        for r in range(len(board)):
            for c in range(len(board)):
                element = board[r][c]
                if (r,element)in res or (element,c) in res or (r//3, c//3, element) in res:
                    return False 
                if element != ".":
                    res.add((r,element))
                    res.add((element,c))
                    res.add((r//3, c//3, element))
        return True 
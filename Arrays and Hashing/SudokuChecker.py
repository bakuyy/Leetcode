class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        state = True

        # check rows
        for i in range(9):
            # check row
            currRow = board[i]
            for n in currRow :
                if n != ".":
                    if currRow.count(n) > 1:
                        state = False    
                        break        
        # check columns
        
        for i in range(9):
            currColumn = [item[i] for item in board]
            for n in currColumn :
                if n != ".":
                    if currColumn.count(n) > 1:
                        state = False   
                        break

        # check grids
        index = 0
        for i in range(9):
            if index >= 9:
                for i in range(3):
                    board.pop(0)
                    index = 0
            currGrid = []
            for m in range(3):
                for n in range(3):
                    currGrid.append(board[m][n+index])
            index += 3
            
            for n in currGrid:    
                if n != ".":
                    if currGrid.count(n) > 1:
                        state = False   
            
        return state
        
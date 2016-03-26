def done_or_not(board):
    if (validRow(board) == False):
        return 'Try again!'
        
    if (validCol(board) == False):
        return 'Try again!'
        
    if (validSquare(board) == False):
        return 'Try again!'
        
    return 'Finished!'
    
def validRow(board):
    for row in board:
        solution = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in row:
            if num in solution:
                solution.remove(num)
            else:    
                return False
    return True
            
def validCol(board):
    counter = -1
    for row in board:
        solution = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counter = counter + 1
        for col in board:  
            if col[counter] in solution:
                solution.remove(col[counter])
            else:    
                return False
    return True
            
def validSquare(board):
    solution = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first = 0
    last = 3
    counter = 0
    for i in range(3):
        for row in board:
            row = row[first:last]   
            if (counter % 3 == 0):
                solution = [1, 2, 3, 4, 5, 6, 7, 8, 9]               
            counter = counter + 1
            for num in row:
                if num in solution:
                    solution.remove(num)
                else:
                    return False
        first = first + 3
        last = last + 3
    return True

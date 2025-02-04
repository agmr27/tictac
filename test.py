import common






def pruneMM(board, turn ,alpha, beta):
    #returns the correct things for wins and ties 
    status = common.game_status(board)
    if  status != None:
        return status
    if all(board):
        return status
    
    #x
    if turn == 1:
        v = -float('inf')
        for index, value in enumerate(board):
            if value==0:
                board[index] = 1
            rval = pruneMM(board, 2, alpha, beta)
            board[index] = 0
            
            if rval ==0:
                rval=-1
            if v ==0:
                v =-1
            v = max(v, rval)
            if v ==-1:
                v=0
            
            # if rval > v:
            #     v = rval
            # if v > alpha:
            #     alpha = v   
       
    if turn == 2:
        v = float('inf')
        for index, value in enumerate(board):
            if value==0:
                board[index] = 2
            rval = pruneMM(board, 1, alpha, beta)
            board[index]=0
            if rval < v:
                v = rval
            if v<beta:
                beta = v
                
    return v




def minmax_tictactoe(board, turn):
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);
    return pruneMM(board, turn, -float('inf'), float('inf'))




##################################################################




def pruneAB(board, turn ,alpha, beta):
    #returns the correct things for wins and ties 
    status = common.game_status(board)
    if  status != None:
        return status
    elif all(board):
        return status
    
    #x
    if turn == 1:
        v = -float('inf')
        for index, value in enumerate(board):
            if value==0:
                board[index] = 1
            rval = pruneAB(board, 2, alpha, beta)
            board[index] = 0
            if rval > v:
                v = rval
            if v >= beta:
                return v
            if v > alpha:
                alpha = v
    if turn == 2:
        v = float('inf')
        for index, value in enumerate(board):
            if value==0:
                board[index] = 2
            rval = pruneAB(board, 1, alpha, beta)
            board[index]=0
            if rval < v:
                v = rval
            if v <= alpha:
                return v
            if v<beta:
                beta = v
                
    return v
                
        


def abprun_tictactoe(board, turn):
    
    
    
    
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);
    # print (prune2(board, turn, -float('inf'), float('inf')))
    return pruneAB(board, turn, -float('inf'), float('inf'))

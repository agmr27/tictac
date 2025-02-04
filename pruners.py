import common



def MMprune (board, turn):
    status = common.game_status(board)
    if status== 0 and 0 not in board:
        return 0
    elif status == 2:
        return 2
    elif status == 1:
        return 1
    
    if turn ==1:
        v = -float('inf')
        for i, value in enumerate(board):
            if  value == 0:
                board[i] = 1
                rval = MMprune(board, 2)
                board[i]=0
                
                if rval ==2:
                    rval =-1
                if v ==2:
                    v =-1
                    
                if rval > v:
                    v = rval
                
                if v ==-1:
                    v =2
    
        return v
    
    
    if turn == 2:
        v = float('inf')
        for i, value in enumerate(board):
            if  value == 0:
                board[i] = 2
                rval = MMprune(board, 1)
                board[i]=0
                
                if rval == 2:
                    rval =-1
                if v == 2:
                    v =-1
                    
                if rval < v:
                    v = rval
                
                if v ==-1:
                    v =2
    
        return v





def minmax_tictactoe(board, turn):
    
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);
    return MMprune(board, turn)


#############################################################################################


def ABprune(board, turn, alpha, beta):
    status = common.game_status(board)
    if status== 0 and 0 not in board:
        return 0
    elif status == 2:
        return 2
    elif status == 1:
        return 1
    
    if turn ==1:
        v = -float('inf')
        for i, value in enumerate(board):
            if  value == 0:
                board[i] = 1
                rval = ABprune(board, 2, alpha, beta)
                board[i]=0
                
                if rval == 2:
                    rval =-1
                if v ==2:
                    v =-1
                    
                if rval > v:
                    v = rval
                    
                if v >= beta:
                    if v ==-1:
                        v = 2
                    return v

                if v > alpha:
                    alpha = v

                if v ==-1:
                    v = 2
    
        return v
    
    
    if turn == 2:
        v = float('inf')
        for i, value in enumerate(board):
            if  value == 0:
                board[i] = 2
                rval = ABprune(board, 1, alpha, beta)
                board[i]=0
                
                if rval == 2:
                    rval =-1
                if v == 2:
                    v =-1
                    
                if rval < v:
                    v = rval
                    
                if v<= alpha:
                    if v ==-1:
                        v = 2
                    return v
                
                if v < beta:
                    beta =v

                if v ==-1:
                    v = 2
    
        return v
    













def abprun_tictactoe(board, turn):
    #put your code here:
    #it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
    #use the function common.game_status(board), to evaluate a board
    #it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
    #the program will keep track of the number of boards evaluated
    #result = common.game_status(board);
    return ABprune(board, turn, -float('inf'), float('inf'))

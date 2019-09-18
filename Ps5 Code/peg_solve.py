DIRECTIONS = {"N": (-1, 0), "E": ( 0, 1), "S": ( 1, 0), "W": ( 0,-1)}
def make_move(B, m, orientation):
    '''
    Apply move m to board B (or inverse if orientation is 'backward')
    Return resulting board, or None if m is not a valid move
    Input:      B | tuple of tuples representing a board configuration
                m | triple representing a board move
      orientation | either 'forward' or 'backward'
    '''
    if m is None: return None
    r, c, d = m
    dr, dc = DIRECTIONS[d]
    R, C = len(B), len(B[0])
    if (0 <= r + 2*dr < R) and (0 <= c + 2*dc < C): # move is on board
        before, after = (1, 1, 0), (0, 0, 1)
        if orientation is "backward": 
            before, after = after, before
        for i in range(3):                          # check that move is valid
            if B[r + i*dr][c + i*dc] != before[i]:
                return None
        B_ = [[p for p in row] for row in B]
        for i in range(3):                          # make move
            B_[r + i*dr][c + i*dc] = after[i]
        return tuple(tuple(p for p in row) for row in B_)

def peg_solve(B,seen=None):
    '''
    Input:  B | tuple of tuples representing a board configuration
    Output: M | tuple of moves to solve B, or None if no such moves exist
    '''  
    if seen==None: seen = set()
    if B in seen: return None

    if solved(B): return ()
    else:
        for row in range(len(B)):
            for col in range(len(B[row])):
                for move in DIRECTIONS:
                    new_board = None
                    if B[row][col]==1: new_board=make_move(B,(row,col,move),"forward")
                    if new_board!=None:
                        if new_board not in seen:
                            recursion = peg_solve(new_board, seen)
                            seen.add(new_board)
                            if type(recursion)==tuple:
                                recursion = ((row,col,move),) + recursion
                                return recursion

def solved(B):
    summ=0
    for row in B:
        for cell in row:
            if cell==1: summ+=1
            if summ>1: return False
    return True

board=[[2,5,0,8,6,0,3,0,9],
        [0,0,0,0,0,3,8,5,1],
        [3,0,0,0,0,0,6,0,7],
        [0,8,0,4,7,0,0,0,6],
        [0,7,4,5,0,6,2,3,0],
        [9,0,0,0,8,1,0,7,0],
        [4,0,9,0,0,0,0,0,2],
        [6,3,5,2,0,0,0,0,0],
        [8,0,7,0,5,4,0,1,3]]

def print_board(board):

    # print column and row
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==len(board[0])-1:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    
    return None

def check_validity(board, number, position):

    #checking validity in particular row
    for i in range(len(board[0])):
        if board[position[0]][i]==number and position[1]!=i:
            return False
    
    #checking validity in particular column
    for i in range(len(board)):
        if board[i][position[1]]==number and position[0]!=i:
            return False
    
    #check validity in sub grid
    start_x=position[1]//3
    start_y=position[0]//3

    for i in range(start_y*3,start_y*3+3):
        for j in range(start_x*3,start_x*3+3):
            if board[i][j]==number and (i,j)!=position:
                return False
    
    return True

def solving(board):
    empty=find_empty(board)
    if not empty:
        return True
    else:
        row,col=empty
    for i in range(1,10):
        if check_validity(board,i,(row,col)):
            board[row][col]=i
            if solving(board):
                return True
            
            board[row][col]=0
    return False

print_board(board)
solving(board)
print_board(board)
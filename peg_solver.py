board=[
    [' ', ' ', 'o', 'o', 'o', ' ', ' '],
	[' ', ' ', 'o', 'o', 'o', ' ', ' '],
	['o', 'o', 'o', 'o', 'o', 'o', 'o'],
	['o', 'o', 'o', '.', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
    [' ', ' ', 'o', 'o', 'o', ' ', ' '],
    [' ', ' ', 'o', 'o', 'o', ' ', ' ']
]

height=len(board)
length=len(board[height-1])
pegs=32
directions=['up','right','down','left']


def print_board():
    for i in range(0,height):
        for j in range(0,length):
            print(str(board[i][j]), end="")
        print("")
    print()

def next_move(row, col, direction):
    cur_move=[[0]*2]*3
    cur_move[0][0]=row
    cur_move[0][1]=col

    if dir=="up":
        cur_move[1][0]=row+1
        cur_move[1][1]=col
        cur_move[2][0]=row+2
        cur_move[2][1]=col
    
    elif dir=="down":
        cur_move[1][0]=row-1
        cur_move[1][1]=col
        cur_move[2][0]=row-2
        cur_move[2][1]=col
    
    elif dir=="right":
        cur_move[1][0]=row
        cur_move[1][1]=col+1
        cur_move[2][0]=row
        cur_move[2][1]=col+2

    else:
        cur_move[1][0]=row
        cur_move[1][1]=col-1
        cur_move[2][0]=row
        cur_move[2][1]=col-2
    
    return cur_move

def is_legal(next_move):
    global board
    if next_move[2][0]>=7 or next_move[2][1]>=7 or next_move[2][0]<0 or next_move[2][1]<0:
        return False
    if board[next_move[0][0]][next_move[0][1]]=='o':
        if board[next_move[1][0]][next_move[1][1]]=='o':
            if board[next_move[2][0]][next_move[2][1]]=='.':
                return True

def make_move(move):
    board[move[0][0]][move[0][1]] = '.'
    board[move[1][0]][move[1][1]] = '.'
    board[move[2][0]][move[2][1]] = 'o'
    
    pegs-=1

def undo_move(move):
    global board
    global pegs
    print("Undo Move")

    board[move[0][0]][move[0][1]] = 'o'
    board[move[1][0]][move[1][1]] = 'o'
    board[move[2][0]][move[2][1]] = '.'
    
    pegs+=1


def find_solution():
    if pegs==1 and board[3][3]=='o':
        print("Solved!")
        print_board(board)
        return True
    else:
        for i in range(0,length):
            for j in range(0, height):
                for k in range(0,len(directions)):
                    move = next_move(j,i,directions[k])
                    if(is_legal(move)):
                        make_move(move)
                        print_board()
                        if find_solution()==True:
                            return True
                        
                        undo_move(move)
        return False
    
def solve_board():
    print_board()

    print("Solving the board")

    solved=find_solution()
    if not solved:
        print("Solution was not found!")

solve_board()



class PegSolitaireSolver:
    def __init__(self):
        self.board=[
                    [' ', ' ', 'o', 'o', 'o', ' ', ' '],
                    [' ', ' ', 'o', 'o', 'o', ' ', ' '],
                    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                    ['o', 'o', 'o', '.', 'o', 'o', 'o'],
                    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                    [' ', ' ', 'o', 'o', 'o', ' ', ' '],
                    [' ', ' ', 'o', 'o', 'o', ' ', ' ']
                ]
        self.height=len(self.board)
        self.length=len(self.board[self.height-1])
        self.pegs=32
        self.directions=['up','right','down','left']
    
    def print_board(self):
        for i in range(0, self.height):
            for j in range(0, self.length):
                print(str(self.board[i][j]), end="")
            print()
        print()
    
    def update_move(self,cur_move, x1, y1,x2,y2):
        cur_move[1][0]=x1
        cur_move[1][1]=y1
        cur_move[2][0]=x2
        cur_move[2][1]=y2

        return cur_move

    
    def next_move(self, row, col, dir):
        cur_move=[[0,0],[0,0],[0,0]]
        cur_move[0][0]=row
        cur_move[0][1]=col

        if dir=="up":
            cur_move=self.update_move(cur_move, x1=row+1, x2=row+2, y1=col, y2=col)
    
        elif dir=="down":
            cur_move=self.update_move(cur_move, x1=row-1, x2=row-2, y1=col, y2=col)
        
        elif dir=="right":
            cur_move=self.update_move(cur_move, x1=row, x2=row, y1=col+1, y2=col+2)

        else:
            cur_move=self.update_move(cur_move, x1=row, x2=row, y1=col-1, y2=col-2)
        
        return cur_move
    
    def is_legal(self, next_move):
        if next_move[2][0] >= 7 or next_move[2][1] >= 7 or next_move[2][0] < 0 or next_move[2][1] < 0:
            return False
        
        return ((self.board[next_move[0][0]][next_move[0][1]] == 'o') and
				(self.board[next_move[1][0]][next_move[1][1]] == 'o') and
				(self.board[next_move[2][0]][next_move[2][1]] == '.'))

    def make_move(self, move):
        self.board[move[0][0]]
        self.board[move[0][0]][move[0][1]] = '.'
        self.board[move[1][0]][move[1][1]] = '.'
        self.board[move[2][0]][move[2][1]] = 'o'
        
        self.pegs-=1
    
    def undo_move(self, move):
        self.board[move[0][0]][move[0][1]] = 'o'
        self.board[move[1][0]][move[1][1]] = 'o'
        self.board[move[2][0]][move[2][1]] = '.'
        
        self.pegs+=1

    def find_solution(self):
        if self.pegs==1 and self.board[3][3]=='o':
            print("Solved")
            self.print_board()
            return True
        else:
            for i in range(0, self.length):
                for j in range(0, self.height):
                    for k in range(0, len(self.directions)):
                        move=self.next_move(j,i,self.directions[k])
                        if(self.is_legal(move)):
                            self.make_move(move)
                            # self.print_board()
                            if self.find_solution()==True:
                                return True
                            
                            self.undo_move(move)
                        
            return False
    
def solve_board():
    solving_object=PegSolitaireSolver()
    
    solving_object.print_board()

    print("Solving the board...")

    if not solving_object.find_solution():
        print("Solution was not found!!")
    
solve_board()

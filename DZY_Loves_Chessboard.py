def beck_tracking(chessboard,x,y):
    # x is the index that represents a current row
    # y is the index that represents a current column

    # check if the chessman isn't in the edge of chessboard
    edge_column = lambda column : True if column in [0,len(chessboard[0])-1] else False

    # check if the chessman is equals to the two adjacent cells
    right_equals = lambda c : True if c == 0 else False
    flag = True if x == len(chessboard) and y == len(chessboard[0]) else False
    
    # considerando que é uma posição valida
    if (flag): # base case):
        if chessboard[x][y] == '.':
            if (not edge_column(y)):
                if (chessboard[x][y+1] == 'B'):
                    chessboard[x][y] = 'W'
                else:
                    chessboard[x][y] = 'B'
            
                if (): # base case
                    return beck_tracking(chessboard,x,y+1)
                else:
                    return beck_tracking(chessboard,x+1,y+1)
            
            else:
                if (right_equals(y)):
                    if (chessboard[x][y-1] == 'B'):
                        chessboard[x][y] = 'W'
                    else:
                        chessboard[x][y] = 'B'
                else:
                    if (chessboard[x][y+1] == 'B'):
                        chessboard[x][y] = 'W'
                    else:
                        chessboard[x][y] = 'B'
                    
                
        #    if (x == len(chessboard)-1 and y == len(chessboard[0])-1): # base case
        #        return chessboard
        

    else: return chessboard

n, m = map(int, input().split()) 
# n meaning number of rows
# m meaning number opf columns

chessboard = []
# matrix that meaning the chessboard

for i in range(n):
    row = input().split()
    chessboard.append(row)

x = 0
y = 0
neo_chessboard = beck_tracking(chessboard,x,y)

print(neo_chessboard)
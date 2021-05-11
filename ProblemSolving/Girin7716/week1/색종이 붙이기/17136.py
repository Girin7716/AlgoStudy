# 색종이 붙이기

# 21% 틀렸습니다
import sys
input = sys.stdin.readline

colorPaper = [0] * 6
board = []
for i in range(10):
    board.append(list(map(int,input().split())))

def check(k,x,y):
    for i in range(k):
        for j in range(k):
            if board[x+i][y+j] != 1:
                return False # 못 붙임
    return True

def glue(k,x,y):    #색종이 붙이기
    for i in range(k):
        for j in range(k):
            board[x+i][y+j] = 0

for k in range(5,0,-1):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1 and ((i+k-1 < 10) and (j+k-1 < 10)):
                if check(k,i,j):
                    colorPaper[k] += 1
                    glue(k,i,j)
    if colorPaper[k] > 5:
        colorPaper[0] = -1
        break
if colorPaper[0] == -1:
    print(-1)
else:
    print(sum(colorPaper))


# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
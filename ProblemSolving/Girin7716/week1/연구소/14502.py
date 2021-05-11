# 연구소
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

rem = []
virus = []
wallCnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            rem.append((i,j))
        elif board[i][j] == 1:
            wallCnt += 1
        elif board[i][j] == 2:
            virus.append((i,j))
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(minVirus):
    cnt = 0 # virus 갯수
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for v in virus:
        q.append(v)

    while q:
        x,y = q.popleft()
        cnt += 1
        if minVirus <= cnt:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 1 or board[nx][ny] == 2 or visited[nx][ny] is True:
                continue
            visited[nx][ny] = True
            q.append((nx,ny))
    return cnt

minVirus = int(1e9)
for comb in combinations(rem,3):
    a,b,c = comb
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1
    minVirus = min(minVirus,bfs(minVirus))
    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    board[c[0]][c[1]] = 0

print((N*M)-minVirus-wallCnt-3)
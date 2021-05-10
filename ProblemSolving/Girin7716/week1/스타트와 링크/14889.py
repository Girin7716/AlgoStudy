# 스타트와 링크
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    S.append(list(map(int,input().split())))

rem = [i for i in range(N)]
comb = list(combinations(rem,N//2))
minValue = int(1e9)

for i in range(len(comb)//2):
    startTeam = 0
    for a,b in combinations(comb[i],2):
        startTeam += (S[a][b] + S[b][a])

    linkTeam = 0
    for a,b in combinations(comb[-i-1],2):
        linkTeam += (S[a][b] + S[b][a])
    minValue = min(minValue,abs(startTeam-linkTeam))
print(minValue)
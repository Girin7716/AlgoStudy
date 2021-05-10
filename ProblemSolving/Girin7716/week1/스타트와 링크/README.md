# 스타트와 링크

## 풀이방법

문제를 보고  N이 최대 20이니까 조합으로 풀 수 있을 것 같았다.



```python
rem = [i for i in range(N)]
comb = list(combinations(rem,N//2))
```

- rem : 축구하는 멤버들
- comb : 축구하는 멤버들을 팀으로 나누는 조합



```python
for i in range(len(comb)//2):
    startTeam = 0
    for a,b in combinations(comb[i],2):
        startTeam += (S[a][b] + S[b][a])

    linkTeam = 0
    for a,b in combinations(comb[-i-1],2):
        linkTeam += (S[a][b] + S[b][a])
    minValue = min(minValue,abs(startTeam-linkTeam))
```

- 위에서 구한 comb을 절반만 검사하면 된다
  - 왜냐하면, 파이썬에서 combinations은 차례대로 조합을 구하기 때문에, (0번째 원소와 마지막 원소)의 원소들이 전부 다른 값이다.
- comb[i]는 startTeam의 멤버로 생각하고 2명씩 조합을 구해서 능력치를 구해서 startTeam에 넣어준다.
- comb[-i-1]은 linkTeam의 멤버로 생각하고 위와 마찬가지로 능력치를 구해서 linkTeam에 넣어준다.
- 그리고 minValue에는 가장 능력치의 차이가 작은 값을 넣어주면 된다.



## 느낀점

문제를 풀면서, 백트래킹으로 풀면 시간 단축할 수 있겠다라고 생각했다.

나중에 시간나면 풀어보겠다.
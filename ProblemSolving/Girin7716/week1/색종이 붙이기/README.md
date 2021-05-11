# 색종이 붙이기_fail

처음에 그리디로 접근해서 가장 큰 색종이부터 확인하면서 붙여가면 된다고 생각했다. 그래서 아래와 같이 코드를 구현했으나 21%에서 틀렸습니다를 받았다.

그리고나서 떠오른 생각이 큰 색종이를 붙인다고 꼭 정답을 보장하지 않는다는 아래의 반례를 통해 사실을 알았다.

```
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

그래서 재귀를 통해 풀어야한다는 사실을 알았으나 구현에 실패했다...

그리하여 인터넷에서 다른 사람들이 푼 코드를 가져와서 그 코드에 주석을 붙이면서 분석하고자한다.

## 풀이방법(다른사람)

출처 : https://chldkato.tistory.com/167

```python
import sys
input = sys.stdin.readline

def func(x, y, cnt):
    global ans	# ans에 최소 색종이 수 저장
	# y가 범위를 벗어나면 재귀가 성공적으로 끝났다는 의미이므로 ans에 최소 색종이 수 저장
    if y >= 10:	
        ans = min(ans, cnt)
        return
	
    # x가 범위를 벗어나면 다음줄을 재귀
    if x >= 10:
        func(0, y+1, cnt)
        return

    # 지금 현 좌표가 색종이를 붙여야하는 곳이라면
    if a[x][y] == 1:
        # 색종이 큰 것부터 검사하면서
        for k in range(5):
            # 해당 사이즈의 색종이가 없으면 불가능
            if paper[k] == 5:
                continue
            # 검사하는 size의 색종이가 바깥으로 넘어가면 불가능
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            # 색종이 붙이는 도중에 0이 포함되어있는지 확인
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    # 색종이 붙이는 중 0이 있으므로 붙이면 안됨
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
			# 해당 size 색종이를 문제없이 붙일 수 있다면
            if not flag:
                # 색종이를 붙이고
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0
				# 해당 색종이 숫자 늘리고
                paper[k] += 1
                # 색종이 붙인 다음 좌표부터 재귀시작하고 색종이 수 + 1
                func(x + k + 1, y, cnt + 1)
                # 색종이 다시 제거하기
                paper[k] -= 1
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1
    # 현 좌표가 0이라서 색종이 붙일 수 없다면 다음 좌표 재귀
    else:
        func(x + 1, y, cnt)


a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
func(0, 0, 0)	#재귀 시작 x,y,cnt
# 만약 ans가 초기값과 같다면 색종이 붙일 수 없으므로 -1 그 외에는 재귀를 통해서 최소 색종이 수를 찾았기때문에 ans 출력
print(ans) if ans != sys.maxsize else print(-1)
```



## 처음에 풀었던 코드(21%에서 틀림)

```python
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
```



## 느낀점

완전탐색을 재귀로 푸는 연습을 해야겠다.
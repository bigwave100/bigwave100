#데이크스트라 알고리즘
#플로이드-워셜 알고리즘 응용
#서강그라운드

n, m, r = map(int, input().split())
inf = 2000
route = [[inf]*n for _ in range(n)]
L = list(map(int, input().split()))
for _ in range(r):
    i, j, rou = map(int, input().split())
    i -= 1
    j -= 1
    if (route[i][j] > rou):
        route[i][j] = rou
    if (route[j][i] > rou):
        route[j][i] = rou

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (i == j):
                route[i][j] = 0
            else :
                if (route[i][j] > route[i][k] + route[k][j]):
                    route[i][j] = (route[i][k] + route[k][j])

M = 0
for i in range(0, n):
    s = 0
    for j in range(0, n):
        if (route[i][j] <= m):
            s += L[j]
    M = max(M, s)
print(M)

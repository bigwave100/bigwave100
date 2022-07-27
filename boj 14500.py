import sys
input = sys.stdin.readline

# 평면의 가로, 세로 길이를 입력받고 평면 안의 데이터를 구성한다.
n, m = map(int, input().split())
L = []
for i in range(n):
    li = list(map(int, input().split()))
    L.append(li)

# 최댓값을 0으로 고정 후 나중에 갱신
M = 0

# 블록 1, 2, 3 모양에 해당하는 값들의 합 저장 후 최댓값 갱신
for i in range(n-2):
    for j in range(m-1):
        s1 = L[i][j] + L[i+1][j] + L[i+1][j+1] + L[i+2][j+1]
        s2 = L[i][j+1] + L[i+1][j] + L[i+1][j+1] + L[i+2][j]
        s3 = L[i][j] + L[i+1][j] + L[i+2][j] + max(L[i][j+1], L[i+1][j+1], L[i+2][j+1])
        s4 = L[i][j+1] + L[i+1][j+1] + L[i+2][j+1] + max(L[i][j], L[i+1][j], L[i+2][j])
        M = max(M, s1, s2, s3, s4)
for i in range(n-1):
    for j in range(m-2):
        s1 = L[i][j+1]+L[i][j+2]+L[i+1][j]+L[i+1][j+1]
        s2 = L[i][j]+L[i][j+1]+L[i+1][j+1]+L[i+1][j+2]
        s3 = L[i][j] + L[i][j+1] + L[i][j+2] + max(L[i+1][j], L[i+1][j+1], L[i+1][j+2])
        s4 = L[i+1][j] + L[i+1][j+1] + L[i+1][j+2] + max(L[i][j], L[i][j+1], L[i][j+2])
        M = max(M, s1, s2, s3, s4)

# 블록 4 모양에 해당하는 값들의 합 저장 후 최댓값 갱신
for i in range(n-1):
    for j in range(m-1):
        s = L[i][j] + L[i+1][j] + L[i][j+1] + L[i+1][j+1]
        M = max(M, s)

# 블록 5 모양에 해당하는 값들의 합 저장 후 최댓값 갱신
for i in range(n):
    for j in range(m-3):
        s = L[i][j] + L[i][j+1] + L[i][j+2] + L[i][j+3]
        M = max(M, s)
for i in range(n-3):
    for j in range(m):
        s = L[i][j] + L[i+1][j] + L[i+2][j] + L[i+3][j]
        M = max(M, s)

# 최댓값 출력
print(M)

import sys
input = sys.stdin.readline

#초기의 입력 값
N, K = map(int, input().split())
start = list(map(int, input().split()))
p = int(input())

#start 행렬을 2차원 구조로 변환
for x in range(K):
    start[x] = [start[x]]
start = start[::-1]

#거듭제곱에 사용될 행렬 생성 (피보나치 수열 응용)
adj = []
adj.append([1]*K)
for y in range(K-1):
    zero_list = [0]*K
    zero_list[y] = 1
    adj.append(zero_list)

#2개의 행렬 곱하는 함수
def multi(a, b):
    func_list = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            tmp_ans = 0
            for k in range(len(a[0])):
                tmp_ans += ((a[i][k]*b[k][j])%p)
                tmp_ans %= p
            func_list[i][j] = tmp_ans
    return func_list

#특정 행렬을 거듭제곱 하는 함수
def power(arr, n):
    if (n == 1):
        return arr
    else:
        if (n%2 == 0):
            return power(multi(arr, arr), n//2)
        else:
            return multi(power(arr, n-1), arr)

#start 행렬에 adj 행렬을 N-K만큼 곱해줌
#완성된 행렬의 [0][0]번째 index가 문제의 답
print(multi(power(adj, N-K), start)[0][0])

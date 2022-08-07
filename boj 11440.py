import sys
input = sys.stdin.readline
mod = 1000000007
adj = [[1, 1], [1, 0]]  #행렬 adj 초기 설정
start = [[1], [1]]      #피보나치 수를 담을 list 초기 설정

#행렬의 곱셈 기능을 하는 함수 multi
def multi(a, b):
    tmp = [[0]*(len(b[0])) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = 0
            for k in range(2):
                s += (a[i][k]*b[k][j])
            tmp[i][j] = (s % mod)
    return tmp

#분할 정복을 위한 함수 power
def power(adj, n):
    if (n == 1):
        return adj
    elif (n%2 != 0):
        return multi(power(adj, (n - 1)), adj)
    else:
        return power(multi(adj, adj), (n // 2))

#N의 값 입력받은 후 피보나치 수의 값 계산
N = int(input())
n_f = 0
if (N < 3):
    n_f = 1
else:
    n_f = multi(power(adj, (N - 2)), start)[0][0]


#행렬 및 피보나치 수 담은 list 초기화
adj = [[1, 1], [1, 0]]
start = [[1], [1]]

#(N+1)의 값 입력받은 후 피보나치 수의 값 계산
N += 1
m_f = 0
if (N < 3):
    m_f = 1
else:
    m_f = multi(power(adj, (N - 2)), start)[0][0]


#피보나치 수의 제곱의 합의 공식에 따른 답 print
print((n_f*m_f) % mod)

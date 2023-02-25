import sys
input = sys.stdin.readline
mod = 998244353

#행렬끼리의 곱셈을 하는 함수
def multi(a, b):
    tmp = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            s = 0
            for k in range(len(a[0])):
                s += (a[i][k]*b[k][j])
            tmp[i][j] = s%mod
    return tmp

#행렬의 제곱을 하는 함수 (Divide and Conquer Algorithm)
def power(adj, n):
    if (n == 1):
        return adj
    else:
        if (n%2 != 0):
            return multi(power(adj, n-1), adj)
        else:
            return power(multi(adj, adj), n//2)





#test-case 수를 받음
t = int(input())

for _ in range(t):
    #제곱 대상 행렬 adj, 결과 값 저장하는 dp인 start
    #start는 adj 여러 개를 곱하며 갱신 예정
    adj = [[0,1,1], [1,0,0], [0,1,0]]
    start = [[1], [1], [1]]

    n = int(input())
    
    #n이 4 미만일 때 결과 값 1 출력 (오류 방지)
    if (n < 4):
        print(1)

    #n이 4 이상일 때, 행렬 adj를 n-3번 만큼 제곱한 값을 start에 곱함
    #결과 행렬의 첫 번째 줄의 첫 번째 원소가 최종 결과 값
    else:
        print(multi(power(adj, n-3), start)[0][0])

import sys
input = sys.stdin.readline
mod = 1000000007

#분할 정복을 이용한 거듭제곱 함수 (divide and conquer)
def squ(n, m):
    if (m == 1):
        return n%mod
    else:
        s = squ(n, m//2)
        if (m%2 == 0):
            return (s*s)%mod
        else:
            return (s*s*n)%mod


#수에 따른 조합을 구하기 위한 dp list 두 개 설정
L = [1]*200001       #factorial dp
inv = [1]*200001     #inverse factorial dp

#factorial dp 값 저장
for i in range(1, 200001):
    L[i] = (i*L[i-1])%mod

#inverse factorial dp 값 저장
inv[200000] = squ(L[200000], mod-2)
for i in range(199999, 0, -1):
    inv[i] = ((i+1)*inv[i+1])%mod

#조합 함수 (위의 dp 두 개 이용)
def comb(n, k):
    a = L[n]
    b = (inv[k]*inv[n-k])%mod
    return (a*b)%mod




#test-case 개수 입력받음
t = int(input())

#수 두 개 입력 받아 포함/배제 원리로 값 계산
#Inclusion-Exclusion Principle

for cnt in range(1, t+1):
    N, M = map(int, input().split())
    N *= 2
    tot = L[N]     #전체 경우 = (2N)!

    #고른 커플 수가 홀수일 경우 결과에서 해당 값 뺌
    #고른 커플 수가 짝수일 경우 결과에서 해당 값 더함
    for i in range(1, M+1):
        tmp = N-i
        ct = comb(M, i)
        tot += (((-1)**i)*squ(2, i)*(L[tmp])*ct)
        tot %= mod
    print("Case #{}: {}".format(cnt, tot))

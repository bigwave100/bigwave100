import sys
input = sys.stdin.readline
mod = 1000000007

#분할 정복을 이용한 거듭제곱 함수 (divide and conquer)
def squ(n, m):
    if (m == 1):
        return (n%mod)
    else:
        s = squ(n, m//2)
        if (m%2 == 0):
            return ((s*s)%mod)
        else:
            return ((s*s*n)%mod)

#순열과 조합을 계산하기 위한 dp
L = [1]*200001          #factorial dp
inv = [1]*200001        #inverse factorial dp

#dp 두 개에 모두 정보 저장
for i in range(1, 200001):
    L[i] = (i*(L[i-1]))
    L[i] %= mod

inv[200000] = squ(L[200000], mod-2)
for i in range(199999, 0, -1):
    inv[i] = ((i + 1)*inv[i + 1])
    inv[i] %= mod


#조합을 계산하는 함수
def comb(n, k):
    a = L[n]
    b = (inv[k]*inv[n-k])%mod
    return ((a*b)%mod)

#순열을 계산하는 함수
def p(n, k):
    c = L[n]
    d = inv[n-k]
    return ((c*d)%mod)




#필요한 n과 k를 입력 받음
n, k = map(int, input().split())

tot = ((p(n, k))**2)%mod       #전체 경우의 수

#고른 경우의 수가 홀수일 땐 tot에서 해당 계산 값을 뺌
#고른 경우의 수가 짝수일 땐 tot에서 해당 계산 값을 더함
#포함/배제의 원리 (Inclusion-Exclusion Principle)
for i in range(1, k+1):
    tot += (((-1)**i)*((comb(k, i)*p(n, i)*p(n-i, k-i)*p(n-i, k-i))%mod))
    tot %= mod

print(tot)

from itertools import combinations
import sys
input = sys.stdin.readline
mod = 1000000007

#오일러 피 함수 응용 (extended euler-phi)
#입력 받은 자연수의 소인수를 모은 list를 return하는 함수
def ouler(n):
    L = []
    for i in range(2, int(n**0.5) + 1):
        if (n%i == 0):
            L.append(i)
            while (n%i == 0):
                n //= i
    if (n > 1):
        L.append(n)
    return L

#유클리드 호제법으로 최대공약수 구하는 함수
def gcd(n, m):
    n, m = max(n, m), min(n, m)
    while (m != 0):
        n, m = m, (n%m)
    return n

#위의 gcd 함수를 이용하여 최소공배수 구하는 함수
def lcm(n, m):
    return (n * m)//gcd(n, m)

#특정 list에 모인 자연수의 최소공배수를 구하는 함수
def LCM(K):
    tmp = K[0]
    for i in range(1, len(K)):
        tmp = lcm(tmp, K[i])
    return tmp




#문제의 조건대로 입력 받음
N, num = map(int, input().split())
C = list(map(int, input().split()))

total = 1           #출력하는 경우의 수 (초기 값 1)

#조건에 따라 total의 값을 갱신
for i in range(N-1):

    #문제의 조건대로 했을 때 나올 수 없는 list C가 입력으로 들어온 경우
    #total에 0 할당 후 break
    if ((C[i]%C[i+1] != 0) or (C[i] < C[i+1]) or (C[i] > num) or (C[i+1] > num)):
        total = 0
        break

    #C[i] == C[i+1]일 경우
    #다음 원소가 num보다 작은 모든 맞는 경우 total에 곱함
    elif (C[i] == C[i+1]):
        total *= (num//C[i+1])
        total %= mod

    #C[i]가 C[i+1]로 나누어 떨어질 경우
    else:
        li = ouler((C[i]//C[i+1]))  #(C[i]//C[i+1])의 소인수들 저장한 list
        k = (num//C[i+1])           #num보다 큰 원소가 경우로 들어가지 않도록 제한
        tot = k            #total에 곱할 값 준비 (초기 값 k)

        #li의 부분 집합들 이용 (combination으로)
        #포함/배제 원리 (Inclusion-Exclusion Principle)
        #해당 부분 집합 원소 개수가 홀수면 그 집합 수들의 최소공배수를 tot에서 뺌
        #해당 부분 집합 원소 개수가 짝수면 그 집합 수들의 최소공배수를 tot에서 더함
        for j in range(1, len(li)+1):
            arr = list(combinations(li, j))
            for K in arr:
                tot += (((-1)**j)*(k//LCM(K)))

        #total에 나온 tot값 곱함
        total *= tot
        total %= mod

#예외 경우 처리
#C의 원소 개수가 한 개일 때 예외 경우
#C[0]이 num보다 크면 total은 0임 (없는 경우이므로)
if ((N == 1) and (C[0] > num)):
    total = 0

#최종 결과 출력
print(total)

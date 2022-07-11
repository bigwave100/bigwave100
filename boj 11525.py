import sys
input = sys.stdin.readline

# 오일러 피 함수
def sol(n) :
    tot = n
    for i in range(2, (int(n**0.5) + 1)) :
        if (n%i == 0) :
            tot *= (1 - (1/i))
            while(n%i == 0) :
                n //= i
    if (n > 1) :
        tot *= (1 - (1/n))
    tot = int(tot)

    return tot



#오일러 피 함수의 값을 담을 리스트 L을 생성한다.
L = [0]*100001
L[0] = 1 ; L[1] = 1    # 나중에 합을 구하기 위해 L[0],L[1] 둘 다 1로 설정

# 리스트 L에 문제의 정수 범위 만큼의 수들의 오일러 피 함수 저장
for k in range(2,100001) :
    L[k] = sol(k)

#dp를 이용하여 오일러 피 함수의 합 저장
for m in range(1,100001) :
    L[m] += L[m-1]

# 출력하고자 하는 값들 b의 값에 따라 L[b]의 값 츨력
T = int(input())
for _ in range(T) :
    a,b = map(int,input().split())
    print(a, L[b])

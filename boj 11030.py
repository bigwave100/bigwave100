import sys
input = sys.stdin.readline
mod = 100000000

#오일러 피 함수
def euler(n):
    tot = n
    for i in range(2, (int(n**0.5) + 1)):
        if (n%i == 0):
            tot *= (1 - (1/i))
            tot = int(tot)
            while (n%i == 0):
                n //= i
    if (n > 1):
        tot *= (1 - (1/n))
        tot = int(tot)
    return tot

#거듭제곱 함수 (나머지 변수에 추가)
def squ(x, y, m):
    if (y == 0):
        return 1%m
    else:
        s = squ(x, y//2, m)
        if (y%2 == 0):
            return (s*s)%m
        else:
            return (s*s*x)%m



#두 양의 정수(<= 20000) 입력 받음
a, b = map(int, input().split())

eul_list = [0]*b       #오일러 피 함수를 이용하여 나눌 수 list
total_list = [0]*b     #생기는 결과 값을 저장하는 list

#eul_list의 i번째 항은 이전 항의 오일러 피 함수 결괏값
eul_list[0] = mod
for i in range(1, b):
    eul_list[i] = euler(eul_list[i-1])



#b == 1일 경우, a 값 mod로 나눈 나머지 출력
if (b == 1):
    ans = a%mod
    print(ans)


#이외의 경우
else:
    #total_list의 마지막 항 값 먼저 저장
    total_list[b-1] = a % eul_list[b-1]
    if (total_list[b-1] == 0):
        total_list[b-1] += eul_list[b-1]    #나머지가 0일 경우 처리

    #마지막 항 값을 이용하여 total_list에 값들 저장
    for k in range(b-2, 0, -1):
        total_list[k] = squ(a, total_list[k+1], eul_list[k])
        if (total_list[k] == 0):
            total_list[k] += eul_list[k]

    #total_list[0]이 최종적으로 구하고자 하는 값
    total_list[0] = squ(a, total_list[1], eul_list[0])
    ans = total_list[0]

    #조건에 맞게 strans 생성 (ans의 문자열 버전)
    if (len(str(ans)) < 8):
        strans = '0'*(8 - len(str(ans))) + str(ans)
    else:
        strans = str(ans)

    #mod로 안 나눴을 때도 답의 길이가 8보다 작다면 ans 그대로 출력
    #이외의 경우는 strans 출력
    if (((b == 2) and (a < 8)) or ((b == 3) and (a < 3)) or (a == 1)):
        print(ans)
    elif ((b == 4) and (a < 3)):
        print(ans)
    else:
        print(strans)

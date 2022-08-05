#오일러 피 함수
#dp
#플래티넘 문제

#오일러 피 함수의 기능을 하는 함수 작성
def ouler(n):
    if (n == 1):
        return 1
    else:
        tot = n
        for i in range(2, (int(n**0.5) + 1)):
            if (n%i == 0):
                tot *= (1 - (1/i))
                while (n%i == 0):
                    n //= i
        if (n > 1):
            tot *= (1 - (1/n))
        return int(tot)

#dp로 임의의 양의 정수 x와 ouler(x)의 값을 곱한 값을 저장
L = [0]*100000
for i in range(100000):
    s = (i+1)*ouler(i+1)
    L[i] = s

#입력 받은 후 문제에서 요구하는 값 출력
n = int(input())

if (n in L):
    print(L.index(n) + 1)
else:
    print(-1)

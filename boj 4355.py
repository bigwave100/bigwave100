import sys
input = sys.stdin.readline

# 오일러 피 함수 구하는 함수 sol(n)
def sol(n) :
    
    if (n == 1) :       # n이 1일 경우 그대로 return
        return n

    else :              # n이 1이 아닐 경우 n의 소인수를 이용하여 오일러 피 함수 계산
        tot = n
        for i in range(2, (int(n**0.5) + 1)) :
            if (n%i == 0) :
                tot *= (1 - (1/i))
                while(n%i == 0) :
                    n //= i
        if (n > 1) :
            tot *= (1 - (1/n))
        return int(tot)



while(True) :           # while 반복문으로 오일러 피 함수 구할 값 여러 번 받음
    n = int(input())

    if (n == 0) :       # n이 0일 때 break
        break
    else :              # n이 자연수일 때 n의 오일러 피 함수 결과값 print
        print(sol(n))

import sys
input = sys.stdin.readline

# 0~n 까지 나오는 0의 개수를 구하기 위한 함수
def sol(n) :
    n = str(n)

    # n이 한 자리일 때 0은 n이 0일때만 나오므로 1을 return한다.
    if (len(n) == 1) :
        return 1

    # n이 두 자리수 이상일 경우, 문자열 슬라이싱을 통하여 계산한다.
    else :
        tot = 0
        L = len(n)

        # 수학적으로 각 자리수에 0이 오는 모든 경우의 수를 계산한다.
        for i in range(L-1,0,-1) :
            if (i == L-1) :
                a = n[:i]
                tot += (int(a) + 1)
            else :
                a = n[i] ; b = n[:i] ; c = n[(i+1):]
                if (int(a) == 0) :
                    tot += ((int(b)-1)*(10**len(c)))
                    tot += (int(c)+1)
                else :
                    tot += (int(b)*(10**len(c)))

        # 0의 총 개수 반환
        return tot



# while 반복문으로 n,m 입력받음
while(True) :
    n,m = map(int,input().split())

    # n이 음수일 경우 while 반복문 break
    if (n < 0) :
        break
    
    else :
        if (n == 0) :          # n이 0일 경우 sol(m)의 값만 계산
            print(sol(m))
        else :                 # n이 0이 아닐 경우, sol(n-1)의 값 뺌
            print(sol(m) - sol(n-1))

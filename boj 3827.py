#행렬 곱셈을 구현한 함수
def multi(a, b, mod):
    L = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            tmp = 0
            for k in range(len(a[0])):
                tmp += ((a[i][k]*b[k][j])%mod)
                tmp %= mod
            L[i][j] = tmp
    return L

#행렬의 거듭제곱을 구현한 함수
def power(arr, n, mod):
    if (n == 1):
        return arr
    else:
        if (n%2 == 0):
            return power(multi(arr, arr, mod), n//2, mod)
        else:
            return multi(power(arr, n-1, mod), arr, mod)



while(True):
    N, M, A, B, C, T = map(int, input().split())
    
    #0이 6개로 입력이 들어올 시 프로그램 종료
    if (N == M == A == B == C == T == 0):
        break

    #Start List 생성
    List = list(map(int, input().split()))
    for x in range(N):
        List[x] = [List[x]]

    #거듭제곱 대상 list 생성
    adj = [[0]*N for _ in range(N)]
    if (N == 1):                    #N = 1일 땐 B만 행렬에 추가
        adj[0][0] = B
    else:                           #이외의 경우
        for y in range(N):
            if (y == 0):            #거듭제곱 대상 행렬의 맨 윗줄은 B, C만 추가
                adj[y][y] = B
                adj[y][y+1] = C
            elif (y == N-1):        #거듭제곱 대상 행렬의 맨 아랫줄은 A, B만 추가
                adj[y][y-1] = A
                adj[y][y] = B
            else:                   #이외의 경우, A, B, C 모두 추가
                adj[y][y-1] = A
                adj[y][y] = B
                adj[y][y+1] = C

    #행렬 거듭제곱이 필요 없을 경우 Start List 그대로 출력
    if (T == 0):
        for p in range(N-1):
            print(List[p][0], end=' ')
        print(List[N-1][0])

    #행렬 거듭제곱 필요시 위의 함수들을 이용하여 새로운 list 생성
    #새로운 list 출력
    else:
        ans_list = multi(power(adj, T, M), List, M)
        for p in range(N-1):
            print(ans_list[p][0], end=' ')
        print(ans_list[N-1][0])

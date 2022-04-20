import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
dp_inc = [1]*n
dp_dec = [1]*n

for i in range(1,n) :
    for j in range(i) :
        if (L[j] < L[i]) :
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)

for i in range(n-2,-1,-1) :
    for j in range(n-1,i,-1) :
        if (L[j] < L[i]) :
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)

M = 1
for k in range(n) :
    if (dp_inc[k] + dp_dec[k] - 1 > M) :
        M = dp_inc[k] + dp_dec[k] - 1
print(M)

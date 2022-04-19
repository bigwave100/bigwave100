import sys
input = sys.stdin.readline

L = [0]*100501
L[1] = 1 ; L[2] = 1

for i in range(3,100501) :
    L[i] = L[i-1] + L[i-2]


T = int(input())

for _ in range(T) :
    x = int(input())

    start = 0 ; end = 100500

    while(True) :
        mid = (start + end)//2

        if (L[mid] == x) :
            print(mid)
            break

        elif (L[mid] > x) :
            end = mid - 1

        else :
            start = mid + 1

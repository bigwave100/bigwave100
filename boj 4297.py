import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

#merge sort 후에 최종 swap 횟수를 계산하는 함수
#recursion으로 구현
def merge_sort(s, e):
    global arr, swap
    size = e - s
    mid = (s + e) // 2
    if (size <= 1):
        return

    merge_sort(s, mid)
    merge_sort(mid, e)

    newArr = []
    idx1, idx2 = s, mid
    cnt = 0
    while ((idx1 < mid) and (idx2 < e)):
        if (arr[idx1] > arr[idx2]):
            newArr.append(arr[idx2])
            idx2 += 1
            cnt += 1
        else:
            newArr.append(arr[idx1])
            idx1 += 1
            swap += cnt

    while (idx1 < mid):
        newArr.append(arr[idx1])
        idx1 += 1
        swap += cnt
    while (idx2 < mid):
        newArr.append(arr[idx2])
        idx2 += 1
        cnt += 1

    for t in range(len(newArr)):
        arr[s + t] = newArr[t]


#각 test-case에서 list에 대한 정보 입력 받음 (list 길이 0이면 종료)
#merge sort 실행 후 최종 swap 횟수 출력
while(True):
    n = int(input())

    if (n == 0):
        break

    else:
        arr = []
        swap = 0
        for _ in range(n):
            arr.append(int(input()))
        merge_sort(0, n)
        print(swap)

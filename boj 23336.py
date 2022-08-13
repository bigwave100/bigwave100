import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

#정수를 담은 list에 대한 정보를 입력받고, swap 횟수 0으로 둠
n = int(input())
arr = list(map(int, input().split()))
swap = 0

#merge sort 실행 및 swap 횟수 계산 함수
#recursion으로 구현
def merge_sort(start, end):
    global arr, swap
    size = end - start
    mid = (start + end) // 2
    if (size <= 1):
        return

    merge_sort(start, mid)
    merge_sort(mid, end)

    newArr = []
    idx1, idx2 = start, mid
    cnt = 0
    while ((idx1 < mid) and (idx2 < end)):
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
        arr[start + t] = newArr[t]


#merge sort 실행 후 저장된 최종 swap 횟수 출력
merge_sort(0, n)

print(swap)

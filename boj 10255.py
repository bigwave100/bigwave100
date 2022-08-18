#ccw 알고리즘의 기본 틀 함수
def ccw(x1, y1, x2, y2, x3, y3):
    s = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
    if (s < 0):
        return -1
    elif (s > 0):
        return 1
    else:
        return 0
#ccw 알고리즘의 기본 틀 함수를 이용한 선분 교차 판별 함수
def sol(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    ccw1 = ccw123 * ccw124
    ccw2 = ccw341 * ccw342

    #선분이 직사각형의 꼭짓점에 걸치는 경우 0.5 return
    #그 외의 한 점에서 만나는 경우 1 return
    #겹치는 경우 4 return
    if (ccw1 == ccw2 == 0):
        if (x1 == x2 == x3 == x4):
            my1, my2, my3, my4 = min(y1, y2), max(y1, y2), min(y3, y4), max(y3, y4)
            if ((my2 == my3) or (my1 == my4)):
                return 0.5
            elif ((my1 <= my4) and (my3 <= my2)):
                return 4
            else:
                return 0
        elif (y1 == y2 == y3 == y4):
            mx1, mx2, mx3, mx4 = min(x1, x2), max(x1, x2), min(x3, x4), max(x3, x4)
            if ((mx2 == mx3) or (mx1 == mx4)):
                return 0.5
            elif ((mx1 <= mx4) and (mx3 <= mx2)):
                return 4
            else:
                return 0
        else:
            return 0.5


    elif ((ccw1 < 0) and (ccw2 == 0)):
        return 1

    elif ((ccw1 == 0) and (ccw2 < 0)):
        return 0.5

    elif ((ccw1 < 0) and (ccw2 < 0)):
        return 1

    else:
        return 0


#test-case별로 선분과 직사각형이 만나는 점의 개수 반환
t = int(input())
for _ in range(t):
    xm, ym, xM, yM = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    xx1, yy1 = xm, yM
    xx2, yy2 = xM, yM
    xx3, yy3 = xM, ym
    xx4, yy4 = xm, ym

    s1 = sol(x1, y1, x2, y2, xx1, yy1, xx2, yy2)
    s2 = sol(x1, y1, x2, y2, xx2, yy2, xx3, yy3)
    s3 = sol(x1, y1, x2, y2, xx3, yy3, xx4, yy4)
    s4 = sol(x1, y1, x2, y2, xx4, yy4, xx1, yy1)
    L = [s1, s2, s3, s4]

    #직사각형의 한 변이라도 선분과 겹치면 4 출력
    if (4 in L):
        print(4)

    #다른 경우, 선분과 직사각형이 만나는 점의 개수 출력
    else:
        s = sum(L)
        print("{:.0f}".format(s))

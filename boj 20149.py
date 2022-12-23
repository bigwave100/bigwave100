#기하학
#선분 교차 판정
#많은 조건 분기
#Platinum IV

#CCW 알고리즘(결과 값의 양수/음수, 0 중에 어떤 것인지 판정
def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if (c < 0):
        return -1
    elif (c > 0):
        return 1
    else:
        return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
flag = 0

#저장되지 않은 변수 초기 값들 none으로 설정
ansx = 'none'; ansy = 'none'    #답의 x, y 좌표
m1 = 'none'; m2 = 'none'        #두 선분의 기울기
X1 = 'none'; X2 = 'none'        #선분이 y축에 평행할 때의 x 값
b1 = 'none'; b2 = 'none'        #선분의 y절편

#위에 none으로 저장해놓은 값들 조건에 따라 갱신
if (x1 == x2):
    X1 = x1
if (x3 == x4):
    X2 = x3
if (x1 != x2):
    m1 = (y2-y1)/(x2-x1)
    b1 = y1 - (m1*x1)
if (x3 != x4):
    m2 = (y4-y3)/(x4-x3)
    b2 = y3 - (m2*x3)

#선분 두 개 각각의 양 끝점을 활용하여 네 개의 ccw 결과 값 생성(위에 정의한 함수 이용)
ccw1 = ccw(x1, y1, x2, y2, x3, y3)
ccw2 = ccw(x1, y1, x2, y2, x4 ,y4)
ccw3 = ccw(x3, y3, x4, y4, x1, y1)
ccw4 = ccw(x3, y3, x4, y4, x2, y2)

#판정을 위해 ccw 결과 값 두 개씩 묶어줌(ccw1, ccw2)
c1 = ccw1*ccw2 ; c2 = ccw3*ccw4


# c1, c2 둘 중 하나라도 양수이면 0 출력
if (c1 > 0 or c2 > 0):
    print(0)

else:
    #c1, c2 모두 0 나올 때
    if (c1 == c2 == 0):
        
        #여기서 두 선분이 서로 떨어져 있으면 0 출력
        if ((max(x1, x2) < min(x3, x4)) or (max(y1, y2) < min(y3, y4)) or (max(x3, x4) < min(x1, x2)) or (max(y3, y4) < min(y1, y2))):
            print(0)

        #선분이 서로 붙어있거나 교차할 때, 겹치면 1만 출력하고 그 외에는 교차점 출력
        else:
            print(1)
            if (m1==m2 and X1==X2 and b1==b2):
                if ((max(x1, x2) > min(x3, x4)) and (max(x3, x4) > min(x1, x2))):
                    flag = 1
                elif (x1 == x3 or x1 == x4):
                    ansx = x1; ansy = y1
                elif (x2 == x3 or x2 == x4):
                    ansx = x2; ansy = y2
            
            if (ansx != 'none'):
                print("{:.10f} {:.10f}".format(ansx, ansy))
            elif (flag == 0):
                ansx = (b2-b1)/(m1-m2)
                ansy = m1*ansx + b1
                print("{:.10f} {:.10f}".format(ansx, ansy))

    #그 외의 경우, 두 선분 각각 y축과의 평행 여부를 확인
    #교점 출력
    else:
        print(1)
        if (m1 == 'none'):
            ansx = X1
            ansy = m2*ansx + b2
        elif (m2 == 'none'):
            ansx = X2
            ansy = m1*ansx + b1
        else:
            ansx = (b2-b1)/(m1-m2)
            ansy = m1*ansx + b1
        print("{:.10f} {:.10f}".format(ansx, ansy))

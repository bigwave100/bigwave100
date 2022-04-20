def Sum(n) :
    n = str(n)

    if (len(n) == 1) :
        n = int(n)
        return ((n*(n+1))//2)

    else :
        ans = 0
        for i in range(len(n)-1,-1,-1) :

            if (i == len(n)-1) :
                a = int(n)//10 ; b = int(n)%10
                ans += ((a*45) + ((b*(b+1))//2))

            elif (i == 0) :
                a = len(n)-1
                b = ((int(n))%(10**a))
                c = int(n[i])
                ans += (c*(b+1))
                ans += (((c*(c-1))//2)*(10**a))

            else :
                a = n[:i]
                b = n[i]
                c = n[(i+1):]
                x = int(a) ; y = int(b) ; z = int(c)

                ans += (x*(10**len(c))*45)
                ans += (((y*(y-1)//2)*(10**len(c))) + (y*(z+1)))

        return ans

n,m = map(int,input().split())

if (n == 0) :
    print(Sum(m))
else :
    print(Sum(m) - Sum(n-1))

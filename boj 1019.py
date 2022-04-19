n = int(input())
L = [0]*10

if (len(str(n)) == 1) :
    for i in range(1,n+1) :
        L[i] = 1

else :
    n = str(n)

    for i in range(len(n)-1,-1,-1) :
        
        if (i == len(n)-1) :
            a = int(n)//10 ; b = int(n)%10
            for j in range(10) :
                L[j] += a
            L[0] -= 1
            for k in range(b+1) :
                L[k] += 1

        elif (i == 0) :
            a = n[i] ; b = n[(i+1):]
            for j in range(1,int(a)) :
                L[j] += (10**len(b))
            L[int(a)] += (int(b) + 1)

        else :
            a = n[:i] ; b = n[i] ; c = n[(i+1):]
            x = int(a) ; y = int(b) ; z = int(c)
            for j in range(1,10) :
                L[j] += (x*(10**len(c)))
            L[0] += ((x-1)*(10**len(c)))
            for k in range(y) :
                L[k] += (10**len(c))
            L[y] += (z+1)

print(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9])

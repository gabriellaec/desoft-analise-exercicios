def calcula_fibonacci(n):
    if n==0:
        L=[]
        return L
    elif n==1:
        L=[1]
        return L
    elif n==2:
        L=[1,1]
        return L
    else:
        L=[1,1]
        i=2
        while i<n:
            a=L[i-1]+L[i-2]
            L.append(a)
            i+=1
        return L
def calcula_fibonacci(n):
    L=[1,1]
    i=0
    while i<n:
        L[i]=L[i-1]+L[i-2]
        i+=1
    return L[ :n-1]
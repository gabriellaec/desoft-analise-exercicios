a[i]=1/(2**i)
a[0]=1
a[1]=1/2
i = 2
while i<101:
    soma = a[0]+a[1]+a[i]
    print(soma)
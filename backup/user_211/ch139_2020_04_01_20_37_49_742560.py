def arcotangente(x,n):
    listatudo=[0]*2*n
    listatudo[0]=x
    listaimpar=[]
    resultado=0
    i=1
    for i in range(1,2*n):
        listatudo[i]=((x**i)/(i))
    print(listatudo)
    listaimpar.append(listatudo[1::2])
    while(i<n):
        resultado=(sum((-1)**i * listaimpar[i]) )
    return resultado


 
print(arcotangente(1,5))
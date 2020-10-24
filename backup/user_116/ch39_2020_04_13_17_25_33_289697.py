n=2
i=2
dicio={}
while n<1001:
    contador=0
    n=i
    while n>1:
        if n%2==0:
            n=n/2
            contador+=1
        else:
            n=n*3+1
            contador+=1
    n=i
    dicio[i]=contador
    i+=1
print(max(dicio,key=dicio.get))
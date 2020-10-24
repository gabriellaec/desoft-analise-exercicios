lista[0]=1
ls=[]
i=0
n=len(lista)
while i<=998:
    lista[i+1]=lista[i]+1
    i+=1
i=0
while i<=n and lista[i]!=1:
    if lista[i]%2==0:
        lista[i]=lista[i]/2
    else:
        lista[i]=lista[i]*3+1
    i+=1    
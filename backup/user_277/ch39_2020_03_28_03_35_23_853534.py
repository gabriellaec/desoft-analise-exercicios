n=int(input('nmr'))
contador=0
i=0
while n>1:
    if n%2==0:
        n=n/2
        contador+=1
    else:
        n=3*n+1
        contador+=1
print (contador)
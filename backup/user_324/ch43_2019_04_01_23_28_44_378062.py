
contador=1
resultado=0
while resultado!=1:
        if n%2==0:
            resultado=n/2
        else:
            resultado=3*n+1
        contador+=1
        n=resultado
        print(resultado)
print(contador)
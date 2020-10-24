numero=int(input("Diga um número inteiro"))
i=0
L=[0]*i
while numero>0:
    L[i]=numero
    numero=int(input("Diga outro número inteiro"))
    i+=1
L.reverse()
print(L)
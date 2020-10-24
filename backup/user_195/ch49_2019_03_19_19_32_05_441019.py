numero=int(input("Diga um número inteiro"))
i=1
L=[numero]
while numero>0:
    L[i-1]=numero
    numero=int(input("Diga outro número inteiro"))
    i+=1
    L.append(0)
    
L.remove(0)
L.reverse()
print(L)
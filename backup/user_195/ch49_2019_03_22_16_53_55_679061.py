numero=int(input("Diga um número inteiro"))
L=[numero]
while numero>0:
    L.append(numero)
    numero=int(input("Diga outro número inteiro"))
L.reverse()
print(L)
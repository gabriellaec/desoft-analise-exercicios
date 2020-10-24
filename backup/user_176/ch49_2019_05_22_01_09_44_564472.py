n = int(input("digite números inteiros positivos"))
lista = []
while n > 0:
    lista.append(n)
    n = int(input("digite números inteiros positivos"))
i = len(lista)-1
if n <= 0:
    print (lista[i])
	i-=1
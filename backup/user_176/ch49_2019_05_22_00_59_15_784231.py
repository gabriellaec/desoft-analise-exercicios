n = int(input("digite números inteiros positivos"))
lista = []
while n > 0:
    lista.append(n)
if n <= 0:
    print (lista[:-1])

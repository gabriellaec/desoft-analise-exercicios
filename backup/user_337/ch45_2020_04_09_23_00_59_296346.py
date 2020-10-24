n = int(input('Digite numeros inteiros positivos: '))
lista = []
while n > 0:
    lista.append(n)
    n = int(input('Digite numeros inteiros positivos: '))

print (lista[::-1])
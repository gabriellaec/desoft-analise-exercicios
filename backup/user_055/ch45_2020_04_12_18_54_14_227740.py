n = int(input('Digite números inteiros positivos: '))
lista_numeros = []
while n > 0:
    lista_numeros.append(n)
    n = int(input('Digite números inteiros positivos: '))
lista_numeros.reverse()
print(lista_numeros)
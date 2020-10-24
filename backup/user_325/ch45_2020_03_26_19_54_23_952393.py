numeros = int(input("Digite numeros inteiros positivos: "))
lista = []
while numeros >= 0:
    numeros = int(input("Digite numeros inteiros positivos: "))
    lista.append(numeros)
print(lista[::-1])
    
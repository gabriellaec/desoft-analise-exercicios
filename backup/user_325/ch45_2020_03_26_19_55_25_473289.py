numeros = int(input("Digite numeros inteiros positivos: "))
lista = []
while numeros >= 0:
    lista.append(numeros)
    numeros = int(input("Digite numeros inteiros positivos: "))
print(lista[::-1])
    
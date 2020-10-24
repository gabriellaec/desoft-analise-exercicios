numeros = int(input("Digite numeros inteiros positivos: "))
lista = []
while numeros >= 0:
    lista.append(numeros)
print(lista[::-1])
    
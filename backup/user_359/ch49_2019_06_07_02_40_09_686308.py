lista_num = []
numeros = int(input("Numeros inteiros e positivos"))
lista_num.append(numeros)
while numeros <= 0:
    numeros = int(input("Numeros inteiros e positivos"))
    lista_num.append(numeros)
print(lista_num[: :-1])
    
lista = []
numero = int(input('Diga um numero inteiro e positivo '))
while numero > 0:
    lista.append(numero)
    numero = int(input('Diga um numero inteiro e positivo '))
i = -1
while i >= -len(lista):
    print(lista[i])
    i = i - 1
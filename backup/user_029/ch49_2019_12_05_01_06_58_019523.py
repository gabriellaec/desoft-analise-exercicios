x = int(input('digite inteiros positivos'))
lista = []
while x > 0:
    lista.append(x)
    x = int (input('digite inteiros positivos'))
print(lista[::-1])
lista = []
n = int(input('Número inteiro: '))
while n > 0:
    lista.append(n)
    n = int(input('Número inteiro: '))
lista = lista[::-1]
print(lista)
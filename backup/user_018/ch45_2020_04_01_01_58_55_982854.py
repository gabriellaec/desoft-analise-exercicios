lista = []
n = int(input('N = '))
while n > 0:
    lista.append(n)
    n = int(input('N = '))
lista = lista[::1]
print(lista)


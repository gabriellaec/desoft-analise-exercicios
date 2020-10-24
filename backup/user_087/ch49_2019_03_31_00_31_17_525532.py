n = int(input('diga um numero '))
lista = []
while n > 0:
    lista.append(n)
    n = int(input('diga um numero '))
lista.reverse()
print(lista)
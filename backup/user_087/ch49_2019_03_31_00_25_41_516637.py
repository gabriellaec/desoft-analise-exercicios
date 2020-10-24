n = int(input('diga um numero '))
lista = []
while n > 0:
    lista.append(n)
    n = int(input('diga um numero '))
print (lista)

print (lista[::-1])
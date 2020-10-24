a = input('palavra')
i = 0
lista = range(100)
while a != 'fim':
    lista[i] = a
    primeira_letra = a[0]
    if primeira_letra == 'a':
        print (a)
    i += 0
    a = input('palavra')
print (lista)
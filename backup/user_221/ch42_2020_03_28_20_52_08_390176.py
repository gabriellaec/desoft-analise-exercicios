lista = []
x = ''
i = 0
while x != 'fim':
    x = input('diga uma palavra ')
    lista.append(x)
    primeira_letra = lista[i][0]
    if primeira_letra == 'a':
        print(lista[i])
    i = i + 1
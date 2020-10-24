lista = []
a = input('digite uma palavra: ')
lista.append(a)
i = 0
while lista[i] != 'fim':
    if lista[i][0] == 'a':
        print(lista[i])
        i += 1
    else:
        del(lista[i])
        a = input('digite outras palavras: ')
        lista.append(a)
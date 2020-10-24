lista = []
palavra = input('Digite uma palavra ')
i = 0
while lista[i] != 'fim':
    lista.append(palavra)
    palavra = input('Digite uma palavra ')
    i += 1
x = 0
while x < len(lista):
    if lista[x][0] == 'a':
        print(lista[x])
        x += 1
    else:
        x += 1

     
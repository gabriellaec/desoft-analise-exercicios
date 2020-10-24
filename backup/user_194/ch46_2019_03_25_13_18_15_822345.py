lista = []
a = input('valor da lista?')

while a != 'fim':
    lista.append(a)
    a = input('valor da lista?')

i = 0
while i < len(lista):
    if lista[i][0] == 'a':
        print(lista[i])
    i += 1
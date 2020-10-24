lista = []
a = input('Palavra:   ')
lista.append(a)
while a != 'fim':
    a = input('Palavra:   ')
i = 0
while i < len(lista):
    if lista[i][1] == 'a':
        print(lista[i][1])
    i += 1
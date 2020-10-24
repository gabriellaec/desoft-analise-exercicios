def letra():
    i = 0
    lista = []
    nova = []
    a = input('Digite uma palavra: ')
    while a != 'fim':
        lista.append(a)
        a = input('Digite uma palavra: ')
    while i < len(lista):
        if lista[i][0] == 'a':
            nova.append(lista[i])
        i += 1
    i = 0
    while i < len(nova):
        print(nova[i])
        i += 1

letra()

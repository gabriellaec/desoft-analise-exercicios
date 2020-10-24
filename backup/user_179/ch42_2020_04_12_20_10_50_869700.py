palavra = str(input('Palavra:'))
lista = []
while palavra != 'fim':
    palavra = str(input('Palavra:'))
    if palavra[1] == 'a':
        lista.append(palavra)

i = 0
while i < len(lista):
    print (lista[i])
    i += 1
    
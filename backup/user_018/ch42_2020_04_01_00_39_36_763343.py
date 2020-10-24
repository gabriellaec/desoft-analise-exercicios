palavra = input('Digite uma palavra: ')
lista = []
while palavra != 'fim':
    if palavra[0] == 'a':
        lista.append(palavra)
    palavra = input('Digite uma palavra: ')
i = 0
while i < len(lista):
    print(lista[i])
    i += 1
    
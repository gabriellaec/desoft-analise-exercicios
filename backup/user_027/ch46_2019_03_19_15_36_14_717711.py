palavra = input('Digita a primeira palavra: ')
lista = []
lista1 = []
while palavra != 'fim':
    lista.append(palavra)
    if palavra[0] == 'a':
        lista1.append(palavra)
    palavra = input('Digite a próxima palavra: ')
cont = 0
while cont < len(lista1):
    print(lista1[cont])
    cont += 1
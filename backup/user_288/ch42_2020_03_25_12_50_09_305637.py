palavra = input ('escreva uma palavra: ')
i = 0
lista = []

while palavra != 'fim':
    lista.append (palavra)
    palavra = input ('escreva uma palavra: ')
while i < len(lista):
    if lista[i][0] == 'a':
        print (lista[i])
    i += 1
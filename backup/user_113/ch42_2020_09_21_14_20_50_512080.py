perg = input('Escreva uma palavra: ')
lista = []
while perg != 'fim':
    lista.append(perg)
    perg = input('Escreva uma palavra: ')

i = 0
while i < len(lista):
    if lista[i] == 'a':
        print(lista)
    i += 1
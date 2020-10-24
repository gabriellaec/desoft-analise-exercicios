perg = input('Escreva uma palavra: ')
lista = []
while perg != 'fim':
    lista.append(perg)
    perg = input('Escreva uma palavra: ')
i = 0
while i < len(lista):
    palavra = lista[i]
    if palavra[0] == 'a':
        print(palavra)
    i += 1
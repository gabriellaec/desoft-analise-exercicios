palavra = input('Escreva uma palavra: ')
lista_palavra = []
lista_palavra.append(palavra)
while palavra != 'fim':
    palavra = input('Escreva outra palavra: ')
    lista_palavra.append(palavra)
i = 0
while i < len(lista_palavra):
    primeira_letra = lista_palavra[i][0]
    if primeira_letra == 'a':
        print(lista_palavra[i])
i += 1 
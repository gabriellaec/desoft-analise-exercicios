palavra = input('Escreva uma palavra: ')
lista_palavra = []
while palavra != 'fim':
    lista_palavra.append(palavra)
    palavra = input('Escreva outra palavra: ')
    i = 0
    while i < len(lista_palavra):
        palavra = lista_palavra[i]
        if len(palavra) > 1 and palavra[0] == 'a':
            print(palavra)
        i += 1
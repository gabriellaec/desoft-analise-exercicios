lista_palavras = []
palavra = input('Escreva uma palavra:')
while palavra != 'fim':
    lista_palavras.append(palavra)
    palavra = input('Escreva outra palavra:')
i = 0
while i <len(lista_palavras):
    palavra = lista_palavras[i]
    if len(palavra) > 0 and palavra[0] == 'a':
        print(palavra)
    i = i + 1
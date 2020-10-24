lista_palavras = []
lista_palavras = input('Insira uma lista de palavras ')
lista_palavras[i] = palavra
palavra = []
i = 0
while palavra != 'fim':
    lista_palavras.append(palavra)
    lista_palavras = input('Insira uma lista de palavras ')
    if palavra[0] == 'a' or palavra[0] == 'A': 
        print(palavra)
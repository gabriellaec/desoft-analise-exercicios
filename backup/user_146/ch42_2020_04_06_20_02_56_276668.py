palavra = input('Escreva uma palavra: ')
while palavra != 'fim':
    lista_palavra = []
    lista_palavra.append(palavra)
i = 0
primeira_letra = palavra[0]
while i < len(lista_palavra):
    if primeira_letra == 'a':
        print(lista_palavra)
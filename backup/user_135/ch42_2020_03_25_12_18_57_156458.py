lista_palavras = []
indice = 0

while True:
    lista_palavras.append(str(input('Escreva uma palavra: ')))
    palavra = list(lista_palavras[indice])
    if palavra[0] == 'a':
        indice = indice + 1
    else:
        del lista_palavras[indice]
    resposta = str(input('Deseja finalizar o programa (fim)?\n'))
    if resposta == 'fim':
        break
        
print (lista_palavras)
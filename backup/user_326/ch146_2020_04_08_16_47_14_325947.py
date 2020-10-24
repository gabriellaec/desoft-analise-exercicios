def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        palavra = i
        print(palavra, 'fim')
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
def conta_ocorrencias(lista):
    dicionario = {}
    soma = 0
    for i in lista:
        palavra = i
        for palavra in lista:
            dicionario[lista[palavra]] = soma + 1
    return dicionario
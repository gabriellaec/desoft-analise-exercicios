def conta_ocorrencias(lista):
    dicionario = {}
    for e in lista:
        if e in dicionario[e]:
            dicionario[e] += 1
        else:
            dicionario[e] = 1
print(dicionario)
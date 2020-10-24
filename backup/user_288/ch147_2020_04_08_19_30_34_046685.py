def conta_ocorrencias (lista):
    dicionario = {}
    for n in lista:
        if not n in dicionario:
            dicionario[n] = 1
        else:
            dicionario[n] += 1
    return dicionario

def mais_frequente(lista):
    ocorrencias = conta_ocorrencias(lista)
    maior = 0
    palavra = ''
    for p,i in dicionario.items():
        if i > maior:
            maior = i
            palavra = p
    return palavra
    
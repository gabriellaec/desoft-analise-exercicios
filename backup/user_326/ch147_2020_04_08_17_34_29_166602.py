def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        palavra = i
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

def mais_frequente(lista):
    dicionario = conta_ocorrencias(lista)
    if len(dicionario) > 1:
        for palavra, numero in dicionario.items():
            for numero2 in dicionario.values():
                if numero > numero2:
                    escolhida = palavra
        return escolhida
    else:
        for palavra in dicionario.keys():
            return palavra
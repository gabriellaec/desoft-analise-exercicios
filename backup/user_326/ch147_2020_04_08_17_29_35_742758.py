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
    print(dicionario)
    for palavra, numero in dicionario.items():
        for numero2 in dicionario.values():
            if numero > numero2:
                print(palavra)
                escolhida = palavra
    return escolhida
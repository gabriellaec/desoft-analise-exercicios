def estritamente_crescente(lista):
    resposta = []
    j = len(resposta) - 1
    i = 0
    while i < len(lista):
        if lista[i] < resposta[j]:
            resposta.append(lista[i])
        j = j - 1
        i = i + 1
    return resposta
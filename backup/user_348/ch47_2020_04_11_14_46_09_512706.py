def estritamente_crescente(lista):
    resposta = []
    i = 0
    while i < len(lista):
        if lista[i+1] > lista[i]:
            resposta.append(i)
        i = i + 1
    return resposta
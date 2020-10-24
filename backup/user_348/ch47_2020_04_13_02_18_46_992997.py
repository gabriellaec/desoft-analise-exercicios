def estritamente_crescente(lista):
    resposta = []
    i = 0
    t = 1
    while i < len(lista):
        if lista[i] < lista[t]:
            resposta.append(lista[i])
            t = t + 1
        i = i + 1
    return resposta
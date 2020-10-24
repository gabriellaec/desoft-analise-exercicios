def estritamente_crescente(lista):
    i = 1
    t = 0
    while i < len(lista):
        if lista[i] > lista[t]:
            resposta.append(lista[i])
            t = t + 1
        i = i + 1
    return resposta
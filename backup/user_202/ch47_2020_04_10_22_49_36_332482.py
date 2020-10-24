def estritamente_crescente(lista):
    resposta = []
    v = 0
    for i in lista:
        if i > v:
            v = i
            resposta.append(i)
    return resposta
            
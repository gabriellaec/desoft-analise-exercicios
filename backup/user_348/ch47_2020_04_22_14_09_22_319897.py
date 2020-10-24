def estritamente_crescente(lista):
    resposta = [lista[0]]
    i = 0
    while i < len(lista):
        if lista[i] > resposta[len(resposta)-1]:
            resposta.append(lista[i])
        i = i + 1
    return resposta
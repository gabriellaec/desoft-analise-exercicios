def estritamente_crescente(lista):
    if len(lista)==0:
        return []
    i = 0
    resposta = [lista[0]]
    while i < len(lista):
        if lista[i] > resposta[len(resposta)-1]:
            resposta.append(lista[i])
        i = i + 1
    return resposta
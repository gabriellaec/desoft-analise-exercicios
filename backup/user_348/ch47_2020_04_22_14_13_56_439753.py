def estritamente_crescente(lista):
    i = 0
    resposta = [lista[i]]
    if len(lista)==0:
        return []
    while i < len(lista):
        if lista[i] > resposta[len(resposta)-1]:
            resposta.append(lista[i])
        i = i + 1
    return resposta
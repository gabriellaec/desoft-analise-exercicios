def estritamente_crescente(lista):
    resposta = []
    for i in (len(lista)-1):
        if lista[i] < lista[i+1]:
            resposta.append(lista[i])
    return resposta
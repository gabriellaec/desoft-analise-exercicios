def estritamente_crescente(lista):
    resposta = []
    i = 0
    while i < (len(lista)-1):
        if lista[i] < lista[i+1]:
            resposta.append(lista[i])
        i = i + 1
    return resposta
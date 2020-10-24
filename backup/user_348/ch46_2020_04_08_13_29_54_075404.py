def numero_no_indice (lista):
    resposta = []
    for i in range(len(lista)):
        if i == lista[i]:
            resposta.append(i)
    return resposta
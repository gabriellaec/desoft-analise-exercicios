def estritamente_crescente(lista):
    resposta = []
    for i in lista:
        if lista[i+1] > lista[i]:
            resposta.append(i)
            return resposta
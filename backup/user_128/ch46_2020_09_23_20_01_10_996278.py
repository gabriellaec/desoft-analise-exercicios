
def numero_no_indice(lista):

    j = 0
    resposta = []

    for i in lista:
        if i == j:
            resposta.append(i)
            j += 1
        else:
            j += 1

    return resposta

print(numero_no_indice([5, 4, 3, 2, 1]))
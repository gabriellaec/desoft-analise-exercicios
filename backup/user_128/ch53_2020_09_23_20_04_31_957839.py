def soma_impares(lista):

    j = 0
    resposta = []
    soma = 0

    for i in lista:
        if i%2 != 0:
            resposta.append(i)
            j += 1
        else:
            j += 1

    for i in resposta:
        soma += i

    return soma

print(soma_impares([1,2,3,4,5,6,7]))
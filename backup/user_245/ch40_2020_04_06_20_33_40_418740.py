def soma_valores(lista):
    soma = 0
    conta = 0
    while conta<len(lista):
        soma += lista[conta]
        conta+=1
    return soma
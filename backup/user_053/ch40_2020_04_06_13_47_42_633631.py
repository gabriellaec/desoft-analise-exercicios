def soma_valores(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

a = [2, 4, 6, 8, 10]
print(soma_valores(a))
def soma_valores(lista):
    soma = 0
    i = 0
    while(i<len(lista)):
        soma = soma + lista[i]
        i = i + 1
    return soma

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(soma_valores(l))
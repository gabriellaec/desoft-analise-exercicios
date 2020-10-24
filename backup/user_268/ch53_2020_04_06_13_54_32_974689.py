def soma_impares(list):
    a = len(list)
    soma = 0
    for i in range(a):
        if list[i]%2 != 0:
            soma+=i
    return soma
            
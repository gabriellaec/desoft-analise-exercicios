def soma_impares(a):
    soma = 0
    for i in range(1,len(a)):
        if a[i]%2 != 0 or a[i] ==1:
            soma += a[i]
    return soma
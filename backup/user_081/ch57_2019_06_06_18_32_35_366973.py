def soma_impares(a):
    soma = 0
    for i in range(1,len(a)):
        if i%2 != 0 or i ==1:
            soma += a[i]
    return soma
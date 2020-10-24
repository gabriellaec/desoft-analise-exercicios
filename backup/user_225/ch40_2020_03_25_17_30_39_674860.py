def soma_valores(a):
    num = len(a)
    soma = 0
    i = 0
    while i < num:
        soma += a[i]
        i = i + 1
    return(soma)
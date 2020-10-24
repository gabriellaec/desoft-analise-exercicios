def soma_impares(a):
    b = 0
    for i in range(len(a)):
        if a[i] % 2 != 0:
            b += a[i]
    return b
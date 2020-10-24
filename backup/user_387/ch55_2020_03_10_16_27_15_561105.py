def encontra_maximo(a):
    b = a[0][0]

    for linha in range(0,3):
        for coluna in range(0,3):
            if a[linha][coluna] > b:
                b = a[linha][coluna]

    return b

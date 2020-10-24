def encontra_maximo(a):
    b = abs(a[0][0])

    for linha in range(0,3):
        for coluna in range(0,3):
            if abs(a[linha][coluna]) > b:
                b = abs(a[linha][coluna])

    return b

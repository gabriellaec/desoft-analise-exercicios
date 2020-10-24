def calcula_total_da_nota(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
    return total
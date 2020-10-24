def calcula_total_da_nota(a,b):
    i = 0
    valor= 0
    while i < len(a):
        valor += a[i]*b[i]
        i += 1
    return valor
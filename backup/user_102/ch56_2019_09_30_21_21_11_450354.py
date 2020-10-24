def calcula_total_da_nota(a,b):
    i = 0
    valor= 0
    while i < len(a):
        valor += a[0]*b[0]
        i += 1
    return valor
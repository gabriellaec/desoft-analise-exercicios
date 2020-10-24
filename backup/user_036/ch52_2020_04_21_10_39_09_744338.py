def calcula_total_da_nota(a,b):
    i = 0
    s = 0
    for i in a:
        s = a[i]*b[i]
        i+=1
    return s
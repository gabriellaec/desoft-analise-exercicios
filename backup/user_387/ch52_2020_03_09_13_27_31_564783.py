def calcula_total_da_nota(a, b):

    c = []
    for num in range(len(a)):
        c.insert(num, float(a[num]) * float(b[num]))

    return(c)

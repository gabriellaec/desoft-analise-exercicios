def calcula_total_da_nota(a, b):

    c = [0]
    for num in range(len(a)):
        c.insert(num, int(a[num]) * int(b[num]))

    return(c)




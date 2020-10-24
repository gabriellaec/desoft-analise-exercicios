def calcula_total_da_nota(a, b):

    c = [0]
    for num in range(len(a)):
        c.insert(num, a[num] * b[num])

    return(c)




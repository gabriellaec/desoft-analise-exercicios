def calcula_total_da_nota(a, b):
    i = 0
    y = []
    while i < len(a):
        y.append(a[i]*b[i])
        i += 1
    j = 0 
    x = 0  
    while j < len(y):
        x = x + y[j]
        j += 1
    return x
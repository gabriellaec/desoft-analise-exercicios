def junta_listas(x):
    a=[0]
    for i in range(len(x)):
        a[i] = x[i] + x[i-1]
    return a
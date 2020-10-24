def junta_listas(x):
    a=[0]
    i=0
    while i < len(x):
        a[i] = x[i] + x[i-1]
        i+=1
    return a